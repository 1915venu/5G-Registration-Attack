import sctp
import socket
from pycrate_asn1dir.NGAP import *

SERVER_IP = "127.0.0.1"
SERVER_PORT = 38412

sock = sctp.sctpsocket_tcp(socket.AF_INET)

try:
    sock.bind((SERVER_IP, SERVER_PORT))
    print(f"SCTP server listening on {SERVER_IP}:{SERVER_PORT}")

    sock.listen(5)

    while True:
        client_sock, client_addr = sock.accept()
        print(f"New connection from {client_addr}\n")

        try:
            data_tuple = client_sock.sctp_recv(1024)

            if not data_tuple:
                print("No data received\n")
                continue

            recieved_encoded_ngap_message = data_tuple[2]
            recieved_decoded_ngap_message = NGAP_PDU_Descriptions.NGAP_PDU
            recieved_decoded_ngap_message.from_aper_ws(recieved_encoded_ngap_message)
            
            print("Data Recieved by AMF is:\n")
            print(f"{recieved_decoded_ngap_message.get_val()}\n")

        except Exception as e:
            print(f"Error during communication with client: {e}\n")

        finally:
            client_sock.close()
            print(f"Connection with {client_addr} closed\n")

except Exception as e:
    print(f"Failed to start SCTP server: {e}\n")

finally:
    sock.close()
    print("Server socket closed")