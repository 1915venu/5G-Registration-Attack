# Custom Packets

This part of the repository contains code that leverages objects and methods, provided by [pycrate](https://github.com/pycrate-org/pycrate) to send custom `NGAP`, `NAS` and `RRC` messages. These scripts were primarily used for debugging purposes during the development of this project.  

## Setup Instructions

- For installation and setup, please refer to the [main](../README.md) README file. 

## Usage

1. Ensure that you have a successfully running core network simulator (e.g. [Open5gs](https://github.com/open5gs/open5gs)) and/or, a radio access network simulator (e.g. [UERANSIM](https://github.com/aligungr/UERANSIM)) set up on your machine.

2. Use these scripts to send custom packets on the same machine.  
e.g. Suppose you want to send a custom `NGAP` request to trigger the registration process in the core network:  

    2.1) Run all core network services in one terminal.

    2.2) Ensure that the `AMF` IP and port are correctly set in `send_ng_setup_req.py` as follows:

    ```sh
    def send_ngap_pdu(ng_setup_req):
        SOURCE_IP = "192.168.58.100"  
        SOURCE_PORT = 51288
        
        DEST_IP = "192.168.58.100"  # Change this to AMF's NGAP Server IP
        DEST_PORT = 9001    # Change this to AMF's NGAP Server Port
    ```

    2.3) In a separate terminal, execute the Python script to send a custom `NGAP` message, without running the RAN simulator, using the following command:

    ```sh
    python3 send_ng_setup_req.py
    ```