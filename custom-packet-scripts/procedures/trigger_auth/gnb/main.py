import sctp
import socket
from pycrate_mobile.NAS import *
from pycrate_asn1dir.NGAP import *
from ngap_utils.decoder import parse_amf_response
from nas_utils.messages import modify_fgmm_req_nas_pdu
from ngap_utils.sender import send_ng_setup_req, send_initial_ue_msg
from ngap_utils.messages import modify_ng_setup_req, modify_init_ue_msg
from shared_utils.constants import SRC_IP, SRC_PORT, DST_IP, DST_PORT, SEPARATOR

def setup_sctp_connection():
    try:
        sock = sctp.sctpsocket_tcp(socket.AF_INET)
        sock.bind((SRC_IP, SRC_PORT))
        sock.connect((DST_IP, DST_PORT))
        print(SEPARATOR)
        print(f"Connected to SCTP server at {DST_IP}:{DST_PORT}")
        
    except:
        print(SEPARATOR)
        raise ValueError("Unable to setup SCTP Connection!")
    
    finally:    
        return sock  

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