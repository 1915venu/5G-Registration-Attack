from pycrate_asn1dir.NGAP import *
from nas_utils.decoding import check_for_NAS, decode_nas
from shared_utils.constants import SEPARATOR

def decode_ngap(ngap_raw_bytes):
    ngap_hex_data = ngap_raw_bytes.hex()

    ngap_packet_bytes = bytes.fromhex(ngap_hex_data)

    ngap_pdu = NGAP_PDU_Descriptions.NGAP_PDU

    ngap_pdu.from_aper_ws(ngap_packet_bytes)

    return ngap_pdu.get_val()

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