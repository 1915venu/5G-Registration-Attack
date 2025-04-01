from rls_utils.encoding import encode_rls_msg
from shared_utils.constants import DST_GNB_IP, DST_GNB_PORT, SEPARATOR

def send_rls_heartbeat(sock, rls_heartbeat_msg, msgType):    
    try:
        sock.sendto(rls_heartbeat_msg, (DST_GNB_IP, DST_GNB_PORT))
        print(SEPARATOR)
        print(f"Sent {msgType} message to the server")
                
    except Exception as e:
        print(SEPARATOR)
        print(f"Failed to send {msgType} message: {e}")
        print(SEPARATOR)

def send_rls_pdu(sock, rrc_msg, msgType, senders_temp_id):
    encoded_rls_msg = encode_rls_msg(msgType, senders_temp_id, rrc_msg)
    # print(encoded_rls_msg)
    
    try:
        sock.sendto(encoded_rls_msg, (DST_GNB_IP, DST_GNB_PORT))
        print(SEPARATOR)
        print(f"Sent {msgType} message to the server")
        
    except Exception as e:
        print(SEPARATOR)
        print(f"Failed to send {msgType} message: {e}")
        print(SEPARATOR)