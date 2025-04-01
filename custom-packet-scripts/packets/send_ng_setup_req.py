import sctp
import struct
import socket
from pycrate_asn1dir.NGAP import *

def modify_ngap_pdu(ng_setup_req):
    
    # print(ng_setup_req.get_proto())
    
    IEs = []
        
    IEs.append({'id': 27, 'criticality': 'reject', 'value': ('GlobalRANNodeID', ('globalGNB-ID', {'pLMNIdentity': b'\x99\xf9\x07', 'gNB-ID': ('gNB-ID', (1, 32))}))})
    IEs.append({'id': 82, 'criticality': 'ignore', 'value': ('RANNodeName', 'UERANSIM-gnb-999-70-1')})
    IEs.append({'id': 102, 'criticality': 'reject', 'value': ('SupportedTAList', [{'tAC': b'\x00\x00\x01', 'broadcastPLMNList': [{'pLMNIdentity': b'\x99\xf9\x07', 'tAISliceSupportList': [ {'s-NSSAI': {'sST': b'\x01'}}, {'s-NSSAI': {'sST': b'\x02'}} ]}]}])})
    IEs.append({'id': 21, 'criticality': 'ignore', 'value': ('PagingDRX', 'v128')})
    pdu_data = ('initiatingMessage', {'procedureCode': 21, 'criticality': 'reject', 'value': ('NGSetupRequest', {'protocolIEs': IEs})})
    
    ng_setup_req.set_val(pdu_data)
    # print(ng_setup_req.to_asn1())

def send_ngap_pdu(ng_setup_req):

    # SOURCE_IP = "127.0.0.1"  
    # SOURCE_PORT = 51288

    # DEST_IP = "127.0.0.1"
    # DEST_PORT = 38412
    
    SOURCE_IP = "192.168.58.100"  
    SOURCE_PORT = 51288
    
    DEST_IP = "192.168.58.100"
    DEST_PORT = 9001

    sock = sctp.sctpsocket_tcp(socket.AF_INET)

    try:
        sock.bind((SOURCE_IP, SOURCE_PORT))
        sock.connect((DEST_IP, DEST_PORT))
        print(f"Connected to SCTP server at {DEST_IP}:{DEST_PORT} \n")

        ngap_ppid_bytes = b"\x3c\x00\x00\x00"
        ngap_ppid = int.from_bytes(ngap_ppid_bytes, byteorder="big")
        # print(f"Setting PPID as: {int.from_bytes(ngap_ppid_bytes, byteorder="little")}")

        sock.sctp_send(msg=ng_setup_req, ppid=ngap_ppid)
        print("Sent NG Setup Request message to the server \n")
        
        response, ancdata, flags, addr = sock.sctp_recv(2048)

    except Exception as e:
        print(f"Failed to connect or send message: {e} \n")

    finally:
        sock.close()


def main():
    ng_setup_req = NGAP_PDU_Descriptions().NGAP_PDU
    
    modify_ngap_pdu(ng_setup_req)
    
    ng_setup_req = ng_setup_req.to_aper()
    
    # print(ng_setup_req.hex())
    
    send_ngap_pdu(ng_setup_req)

if __name__ == "__main__":
    main()
