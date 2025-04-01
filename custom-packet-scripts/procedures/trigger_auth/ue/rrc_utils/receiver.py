from shared_utils.constants import SEPARATOR

def receive_broadcasted_mib(sock, msgType):
    print(SEPARATOR)
    
    mib = sock.recv(1024)
    print(f"Recieved {msgType} from gNB!")    

def receive_broadcasted_sib1(sock, msgType):
    print(SEPARATOR)
        
    sib1 = sock.recv(1024)    
    print(f"Recieved {msgType} from gNB!")  