import socket
from pycrate_mobile.NAS import *

def modify_nas_pdu(reg_msg):
    reg_msg['5GMMHeader']['EPD'].set_val(126)
    reg_msg['5GMMHeader']['spare'].set_val(0)
    reg_msg['5GMMHeader']['SecHdr'].set_val(0)
    reg_msg['5GMMHeader']['Type'].set_val(65)
    
    # print("debug\n")
    # print(reg_msg['NAS_KSI']._IE_stat)
    # print(reg_msg['NAS_KSI']._IE)
    # print("\n")
    
    reg_msg['NAS_KSI'].set_IE(val={'TSC': 0, 'Value': 7})
    reg_msg['5GSRegType'].set_IE(val={'FOR': 1, 'Value': 1})
    reg_msg['5GSID']['L'].set_val(53)
    reg_msg['5GSID'].set_IE(val= {'spare': 0, 'Fmt': 0, 'Type': 1, 'Value': {
            'PLMN': bytes.fromhex('99f907'),
            'RoutingInd': '0000',
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
    # print(reg_msg._opts)
    # print("\n")
    
    reg_msg['UESecCap'].set_trans(False)
    
    reg_msg['UESecCap']['T'].set_val(46)
    reg_msg['UESecCap']['L'].set_val(4)    
    reg_msg['UESecCap'].set_IE(val={
        '5G-EA0': 1, '5G-EA1_128': 1, '5G-EA2_128': 1, '5G-EA3_128': 1,
        '5G-EA4': 0, '5G-EA5': 0, '5G-EA6': 0, '5G-EA7': 0,
        '5G-IA0': 1, '5G-IA1_128': 1, '5G-IA2_128': 1, '5G-IA3_128': 1,
        '5G-IA4': 0, '5G-IA5': 0, '5G-IA6': 0, '5G-IA7': 0,
        'EEA0': 1, 'EEA1_128': 1, 'EEA2_128': 1, 'EEA3_128': 1,
        'EEA4': 0, 'EEA5': 0, 'EEA6': 0, 'EEA7': 0,
        'EIA0': 1, 'EIA1_128': 1, 'EIA2_128': 1, 'EIA3_128': 1,
        'EIA4': 0, 'EIA5': 0, 'EIA6': 0, 'EIA7': 0
    }) 
    
def send_nas_pdu(reg_msg):
    UDP_IP = "192.168.58.101"  
    UDP_PORT = 4997 

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.sendto(reg_msg, (UDP_IP, UDP_PORT))
    print(f"Sent reg_msg to {UDP_IP}:{UDP_PORT}\n")

    sock.close()

def main():
    
    reg_msg = FGMMRegistrationRequest()

    # print(show(reg_msg)) 
    # print("\n")

    # print(reg_msg.to_bytes)
    # print("\n")
    # print(reg_msg.to_json)
    # print("\n")

    modify_nas_pdu(reg_msg)

    # print(show(reg_msg)) 
    # print("\n")
    
    reg_msg = reg_msg.to_bytes()
    
    send_nas_pdu(reg_msg)

if __name__ == "__main__":
    main()