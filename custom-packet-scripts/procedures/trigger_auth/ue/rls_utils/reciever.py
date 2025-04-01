from shared_utils.constants import SEPARATOR
from rls_utils.decoding import check_mib_or_sib1

def recv_rls_heartbeat(sock, msgType):
    rls_heartbeat_ack = None
    
    try:        
        while rls_heartbeat_ack is None:
            # sock.settimeout(3)
            rls_heartbeat_ack = sock.recv(2048)
            rls_heartbeat_ack = check_mib_or_sib1(rls_heartbeat_ack)
        
    except Exception as e:
        print(SEPARATOR)
        print(f"Failed to receive {msgType} message: {e}")
        print(SEPARATOR)

    return rls_heartbeat_ack

def recv_rls_pdu(sock, msgType):
    rrc_res = None
    
    try:
        while rrc_res is None:
            # sock.settimeout(3)
            rrc_res = sock.recv(2048)
            rrc_res = check_mib_or_sib1(rrc_res)
        
    except Exception as e:
        print(SEPARATOR)
        print(f"Failed to receive {msgType} message: {e}")
        print(SEPARATOR)

    return rrc_res