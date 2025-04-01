import random
import socket
from pycrate_mobile.NAS import *
from pycrate_asn1dir import RRCNR
from rls_utils.encoding import encode_rls_msg
from rls_utils.decoding import parse_gnb_response
from rls_utils.constants import RLS_MSG_TYPE_NAME
# from rrc_utils.constants import RRC_MSG_TYPE_NAME
from rls_utils.sender import send_rls_heartbeat, send_rls_pdu
from rls_utils.reciever import recv_rls_heartbeat, recv_rls_pdu
from shared_utils.constants import SRC_UE_IP, SRC_UE_PORT, SEPARATOR  
# from rrc_utils.receiver import receive_broadcasted_mib, receive_broadcasted_sib1
from rrc_utils.messages import modify_rrc_setup_req, modify_nas_pdu, modify_rrc_reg_req

def setup_udp_connection():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((SRC_UE_IP, SRC_UE_PORT))
        print(SEPARATOR)
        print(f"Connected to UDP client at {SRC_UE_IP} and {SRC_UE_PORT}")
        
    except:
        print(SEPARATOR)
        raise ValueError("Unable to setup UDP Connection!")

    finally: 
        return sock  

def main():
    
    sock = setup_udp_connection()
    
    msg_type_name = RLS_MSG_TYPE_NAME["heartbeat"]
    senders_temp_id = random.getrandbits(64)
    rls_heartbeat_msg = encode_rls_msg(msg_type_name, senders_temp_id)
    
    if rls_heartbeat_msg is None:
        print(SEPARATOR)
        raise ValueError(f"Failed to create {msg_type_name} Message!")
    
    send_rls_heartbeat(sock, rls_heartbeat_msg, msg_type_name)
    
    msg_type_name = RLS_MSG_TYPE_NAME["heartbeat_ack"]
    rls_heartbeat_ack = recv_rls_heartbeat(sock, msg_type_name)
    
    if rls_heartbeat_ack is None:
        print(SEPARATOR)
        raise ValueError(f"No {msg_type_name} received from gNB! RLS connection can't be setup")
    
    parse_gnb_response(rls_heartbeat_ack, msg_type_name)
    
    # msg_type_name = RRC_MSG_TYPE_NAME["master_information_block"]
    # receive_broadcasted_mib(sock, msg_type_name)
    
    # msg_type_name = RRC_MSG_TYPE_NAME["system_information_block_type_1"]
    # receive_broadcasted_sib1(sock, msg_type_name)
    
    msg_type_name = RLS_MSG_TYPE_NAME["rrc_setup_req"]
    rrc_setup_req = RRCNR.NR_RRC_Definitions.UL_CCCH_Message
    modify_rrc_setup_req(rrc_setup_req)
    rrc_setup_req = rrc_setup_req.to_uper()
    
    send_rls_pdu(sock, rrc_setup_req, msg_type_name, senders_temp_id)
    
    msg_type_name = RLS_MSG_TYPE_NAME["rrc_setup_res"]
    rrc_setup_res = recv_rls_pdu(sock, msg_type_name)
        
    if rrc_setup_res is None:
        print(SEPARATOR)
        raise ValueError(f"No {msg_type_name} received from gNB!")
    
    rrc_transaction_id = None
    rrc_transaction_id = parse_gnb_response(rrc_setup_res, msg_type_name)
    
    if rrc_transaction_id is None:
        print(SEPARATOR)
        raise ValueError(f"Unable to retrieve RRC Transaction Identifier!")
    
    reg_nas_pdu = FGMMRegistrationRequest()
    # print(f"{show(reg_nas_pdu)}\n") 
    # print(f"{reg_nas_pdu.to_bytes}\n")
    # print(f"{reg_nas_pdu.to_json}\n")
    modify_nas_pdu(reg_nas_pdu)
    # print(f"{show(reg_nas_pdu)}\n") 
    reg_nas_pdu = reg_nas_pdu.to_bytes()
    
    msg_type_name = RLS_MSG_TYPE_NAME["rrc_reg_req"]
    rrc_reg_req = RRCNR.NR_RRC_Definitions.UL_DCCH_Message
    modify_rrc_reg_req(rrc_reg_req, reg_nas_pdu, rrc_transaction_id)
    rrc_reg_req = rrc_reg_req.to_uper()
    # print(rrc_reg_req)
        
    send_rls_pdu(sock, rrc_reg_req, msg_type_name, senders_temp_id)
    
    msg_type_name = RLS_MSG_TYPE_NAME["auth_req"]
    auth_req = recv_rls_pdu(sock, msg_type_name)
    
    if auth_req is None:
        print(SEPARATOR)
        raise ValueError(f"No {msg_type_name} received from gNB!")
    
    parse_gnb_response(auth_req, msg_type_name)
    
    print(SEPARATOR)

if __name__ == "__main__":
    main()