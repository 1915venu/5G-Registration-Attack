from ngap_utils.constants import NGAP_PPID
from shared_utils.constants import SEPARATOR

def send_ng_setup_req(sock, ng_setup_req):

    ng_setup_res = None

    try:
        ngap_ppid = int.from_bytes(NGAP_PPID, byteorder="big")
        # print(f"Setting PPID as: {int.from_bytes(NGAP_PPID, byteorder="little")}")
        # print(ng_setup_req)

        sock.sctp_send(msg=ng_setup_req, ppid=ngap_ppid)
        print(SEPARATOR)
        print("Sent NG Setup Request message to the server")
        
        ng_setup_res = sock.sctp_recv(1024)
        # print("Returned Len: ", len(ng_setup_res))
        # print(ng_setup_res)

    except Exception as e:
        print(SEPARATOR)
        print(f"Failed to send NG Setup Request message: {e}")
        print(SEPARATOR)
        
    return ng_setup_res

def send_initial_ue_msg(sock, init_ue_msg):
    auth_req = None
    
    try:
        ngap_ppid = int.from_bytes(NGAP_PPID, byteorder="big")
        # print(f"Setting PPID as: {int.from_bytes(NGAP_PPID, byteorder="little")}")
        # print(init_ue_msg)

        sock.sctp_send(msg=init_ue_msg, ppid=ngap_ppid)
        print(SEPARATOR)
        print("Sent Inital UE Message to the server")
        
        auth_req = sock.sctp_recv(1024)
        # print("Returned Len: ", len(auth_req))
        # print(auth_req)

    except Exception as e:
        print(SEPARATOR)
        print(f"Failed to send Inital UE message: {e}")
        print(SEPARATOR)
            
    return auth_req