import time
import sctp
import json
import struct
import socket
from pycrate_mobile.NAS import *
from pycrate_asn1dir.NGAP import *

SEPARATOR = "\n" + "-" * 100 + "\n"

def setup_sctp_connection():
    # SOURCE_IP = "127.0.0.1"  
    # SOURCE_PORT = 51288

    # DEST_IP = "127.0.0.1"
    # DEST_PORT = 38412
    
    SOURCE_IP = "192.168.58.100"  
    SOURCE_PORT = 51288
    
    DEST_IP = "192.168.58.100"
    DEST_PORT = 9001
    
    try:
        sock = sctp.sctpsocket_tcp(socket.AF_INET)
        sock.bind((SOURCE_IP, SOURCE_PORT))
        sock.connect((DEST_IP, DEST_PORT))
        print(SEPARATOR)
        print(f"Connected to SCTP server at {DEST_IP}:{DEST_PORT}")
        
    except:
        print(SEPARATOR)
        raise ValueError("Unable to setup SCTP Connection!")
    
    finally:    
        return sock

def modify_ng_setup_req(ng_setup_req):
    # print(ng_setup_req.get_proto())
    
    IEs = []
        
    IEs.append({'id': 27, 'criticality': 'reject', 'value': ('GlobalRANNodeID', ('globalGNB-ID', {'pLMNIdentity': b'\x99\xf9\x07', 'gNB-ID': ('gNB-ID', (1, 32))}))})
    IEs.append({'id': 82, 'criticality': 'ignore', 'value': ('RANNodeName', 'UERANSIM-gnb-999-70-1')})
    IEs.append({'id': 102, 'criticality': 'reject', 'value': ('SupportedTAList', [{'tAC': b'\x00\x00\x01', 'broadcastPLMNList': [{'pLMNIdentity': b'\x99\xf9\x07', 'tAISliceSupportList': [ {'s-NSSAI': {'sST': b'\x01'}}, {'s-NSSAI': {'sST': b'\x02'}} ]}]}])})
    IEs.append({'id': 21, 'criticality': 'ignore', 'value': ('PagingDRX', 'v128')})
    pdu_data = ('initiatingMessage', {'procedureCode': 21, 'criticality': 'reject', 'value': ('NGSetupRequest', {'protocolIEs': IEs})})
    
    ng_setup_req.set_val(pdu_data)
    # print(ng_setup_req.to_asn1())

def send_ng_setup_req(sock, ng_setup_req):

    ng_setup_res = None

    try:
        ngap_ppid_bytes = b"\x3c\x00\x00\x00"
        ngap_ppid = int.from_bytes(ngap_ppid_bytes, byteorder="big")
        # print(f"Setting PPID as: {int.from_bytes(ngap_ppid_bytes, byteorder="little")}")
        # print(f"{ng_setup_req}\n")

        sock.sctp_send(msg=ng_setup_req, ppid=ngap_ppid)
        print(SEPARATOR)
        print("Sent NG Setup Request message to the server")
        
        ng_setup_res = sock.sctp_recv(1024)
        # print(f"{ng_setup_res}\n")

    except Exception as e:
        print(SEPARATOR)
        print(f"Failed to send NG Setup Request message: {e}")
        print(SEPARATOR)
        
    return ng_setup_res

def decode_ngap(ngap_raw_bytes):
    ngap_hex_data = ngap_raw_bytes.hex()

    ngap_packet_bytes = bytes.fromhex(ngap_hex_data)

    ngap_pdu = NGAP_PDU_Descriptions.NGAP_PDU

    ngap_pdu.from_aper_ws(ngap_packet_bytes)

    return ngap_pdu.get_val()

def check_for_NAS(ngap_data):
    try:
        message_type, message_content = ngap_data
        if "protocolIEs" in message_content["value"][1]:  
            for ie in message_content["value"][1]["protocolIEs"]:
                if ie["id"] == 38:  
                    return ie["value"][1]  
    except Exception as e:
        print(SEPARATOR)
        print(f"Error extracting NAS-PDU: {e}")
        print(SEPARATOR)

    return None

def decode_nas(nas_pdu_bytes):
    hex_data = nas_pdu_bytes.hex()
    
    Msg, err = parse_NAS_MO(unhexlify(hex_data))
    
    if err:
        print(SEPARATOR)
        raise ValueError("Unable to decode NAS message!")
    
    return json.dumps(json.loads(Msg.to_json()), separators=(',', ':'))

def parse_amf_response(amf_res, msg_type):
    print(SEPARATOR)
    # print(f"{amf_res}\n")
    
    (amf_info, flags, ngap_pdu, sctp_info) = amf_res

    amf_ip, amf_port = amf_info
    
    print(f"{msg_type} received from AMF is:")
    print("\nAMF IP: ", amf_ip)
    print("\nAMF Port: ", amf_port)
    print("\nFlag: ", flags)
    
    ngap_data = decode_ngap(ngap_pdu)
    print("\nNGAP Data: ", ngap_data)
    
    nas_pdu = check_for_NAS(ngap_data)
    if nas_pdu is not None:
        nas_data = decode_nas(nas_pdu)
        print("\nNAS Data: ", nas_data)
    
    print("\nSCTP Info:")
    print("  Stream ID:", sctp_info.stream)
    print("  SSN:", sctp_info.ssn)
    print("  Flags:", sctp_info.flags)
    print("  PPID:", sctp_info.ppid)
    print("  Context:", sctp_info.context)
    print("  TSN:", sctp_info.tsn)
    print("  Cum TSN ACK:", sctp_info.cumtsn)
    print("  Association ID:", sctp_info.assoc_id)  
    
def modify_fgmm_req_nas_pdu(fgmm_reg_req_nas_pdu):
    fgmm_reg_req_nas_pdu['5GMMHeader']['EPD'].set_val(126)
    fgmm_reg_req_nas_pdu['5GMMHeader']['spare'].set_val(0)
    fgmm_reg_req_nas_pdu['5GMMHeader']['SecHdr'].set_val(0)
    fgmm_reg_req_nas_pdu['5GMMHeader']['Type'].set_val(65)
    
    # print("debug\n")
    # print(fgmm_reg_req_nas_pdu['NAS_KSI']._IE_stat)
    # print(fgmm_reg_req_nas_pdu['NAS_KSI']._IE)
    # print("\n")
        
    fgmm_reg_req_nas_pdu['5GSRegType'].set_IE(val={'FOR': 1, 'Value': 1})
    fgmm_reg_req_nas_pdu['NAS_KSI'].set_IE(val={'TSC': 0, 'Value': 7})
    fgmm_reg_req_nas_pdu['5GSID']['L'].set_val(53)
    fgmm_reg_req_nas_pdu['5GSID'].set_IE(val= {'spare': 0, 'Fmt': 0, 'Type': 1, 'Value': {
            'PLMN': bytes.fromhex('99f907'),
            'RoutingInd': b'\x00\x00',
            'spare': 0,
            'ProtSchemeID': 1,
            'HNPKID': 1,
            'Output': {
                'ECCEphemPK': bytes.fromhex('f65e929e1b4851b7d5681cd3764bad551bc6d92ced536e2d73395decbe3d2933'),
                'CipherText': bytes.fromhex('c351b27b39'),
                'MAC': bytes.fromhex('3f4038c4497b0db4')
            }
        }
    })
    
    # print("debug\n")
    # print(fgmm_reg_req_nas_pdu._opts)
    # print("\n")
    
    fgmm_reg_req_nas_pdu['UESecCap'].set_trans(False)
    
    fgmm_reg_req_nas_pdu['UESecCap']['T'].set_val(46)
    fgmm_reg_req_nas_pdu['UESecCap']['L'].set_val(4)    
    fgmm_reg_req_nas_pdu['UESecCap'].set_IE(val={
        '5G-EA0': 1, '5G-EA1_128': 1, '5G-EA2_128': 1, '5G-EA3_128': 1,
        '5G-EA4': 0, '5G-EA5': 0, '5G-EA6': 0, '5G-EA7': 0,
        '5G-IA0': 1, '5G-IA1_128': 1, '5G-IA2_128': 1, '5G-IA3_128': 1,
        '5G-IA4': 0, '5G-IA5': 0, '5G-IA6': 0, '5G-IA7': 0,
        'EEA0': 1, 'EEA1_128': 1, 'EEA2_128': 1, 'EEA3_128': 1,
        'EEA4': 0, 'EEA5': 0, 'EEA6': 0, 'EEA7': 0,
        'EIA0': 1, 'EIA1_128': 1, 'EIA2_128': 1, 'EIA3_128': 1,
        'EIA4': 0, 'EIA5': 0, 'EIA6': 0, 'EIA7': 0
    }) 

def modify_init_ue_msg(init_ue_msg, fgmm_reg_req_nas_pdu):
    # print(init_ue_msg.get_proto())
    
    curTime = int(time.time()) + 2208988800
    
    IEs = []
    
    IEs.append({'id': 85, 'criticality': 'reject', 'value': ('RAN-UE-NGAP-ID', 1)})
    IEs.append({'id': 38, 'criticality': 'reject', 'value': ('NAS-PDU', fgmm_reg_req_nas_pdu)})
    IEs.append({'id': 121, 'criticality': 'reject', 'value': ('UserLocationInformation', ('userLocationInformationNR', {'nR-CGI': {'pLMNIdentity': b'\x99\xf9\x07', 'nRCellIdentity': (16, 36)}, 'tAI': {'pLMNIdentity': b'\x99\xf9\x07', 'tAC': b'\x00\x00\x01' }, 'timeStamp': struct.pack("!I",curTime)}))})
    IEs.append({'id': 90, 'criticality': 'ignore', 'value': ('RRCEstablishmentCause', 'mo-Signalling')})
    IEs.append({'id': 112, 'criticality': 'ignore', 'value': ('UEContextRequest', 'requested')})
    pdu_data = ('initiatingMessage', {'procedureCode': 15, 'criticality': 'ignore', 'value': ('InitialUEMessage', {'protocolIEs': IEs})})
        
    init_ue_msg.set_val(pdu_data)
        
def send_initial_ue_msg(sock, init_ue_msg):
    auth_req = None
    
    try:
        ngap_ppid_bytes = b"\x3c\x00\x00\x00"
        ngap_ppid = int.from_bytes(ngap_ppid_bytes, byteorder="big")
        # print(f"Setting PPID as: {int.from_bytes(ngap_ppid_bytes, byteorder="little")}")
        # print(f"{init_ue_msg}\n")

        sock.sctp_send(msg=init_ue_msg, ppid=ngap_ppid)
        print(SEPARATOR)
        print("Sent Inital UE Message to the server")
        
        auth_req = sock.sctp_recv(1024)
        # print(f"{auth_req}\n")

    except Exception as e:
        print(SEPARATOR)
        print(f"Failed to send Inital UE message: {e}")
        print(SEPARATOR)
            
    return auth_req

def main():
    
    sock = setup_sctp_connection()
    
    ng_setup_req = NGAP_PDU_Descriptions().NGAP_PDU
    modify_ng_setup_req(ng_setup_req)
    # print(ng_setup_req.hex())
    ng_setup_req = ng_setup_req.to_aper()
    
    ng_setup_res = send_ng_setup_req(sock, ng_setup_req)
    if ng_setup_res is None:
        print(SEPARATOR)
        raise ValueError("No NG Setup Response received from AMF!")
    
    parse_amf_response(ng_setup_res, "NG Setup Response")
    
    fgmm_reg_req_nas_pdu = FGMMRegistrationRequest()
    modify_fgmm_req_nas_pdu(fgmm_reg_req_nas_pdu)
    fgmm_reg_req_nas_pdu = fgmm_reg_req_nas_pdu.to_bytes()
    # print(f"{fgmm_reg_req_nas_pdu}\n")
    
    init_ue_msg = NGAP_PDU_Descriptions().NGAP_PDU
    modify_init_ue_msg(init_ue_msg, fgmm_reg_req_nas_pdu)
    init_ue_msg = init_ue_msg.to_aper()
    
    auth_req = send_initial_ue_msg(sock, init_ue_msg)
    if auth_req is None:
        print(SEPARATOR)
        raise ValueError("No Authentication Request received from AMF!")
    
    parse_amf_response(auth_req, "Authentication Request")
    
    sock.close()

if __name__ == "__main__":
    main()