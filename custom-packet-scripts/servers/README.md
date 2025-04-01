# Custom Servers

This part of the repository contains servers that leverages objects and methods, provided by [pycrate](https://github.com/pycrate-org/pycrate) to receive and decode `NGAP` messages. These test servers were primarily used for debugging purposes, during the development of this project.   

## Setup Instructions

- For installation and setup, please refer to the [main](../README.md) README file. 

## Usage

1. Ensure that the `AMF` IP and port are correctly set in `test_amf.py` as follows:

```sh
SERVER_IP = "127.0.0.1" # Change this to AMF's NGAP Server IP
SERVER_PORT = 38412 # Change this to AMF's NGAP Server Port 
```

2. Run the Python scripts to start the dummy `AMF` server, using the following command:
  
```sh
python3 test_amf.py
```

3. Ensure that the client scripts have IP and Port configurations, as per the server script above.
   
    e.g. Suppose you want to use send_ng_setup.py from [here](../packets/send_ng_setup_req.py), to send dummy NGAP requests.

    3.1) Ensure that the client script sends NGAP request to the above `AMF` IP and Port as:

    ```sh
    def send_ngap_pdu(ng_setup_req):
        SOURCE_IP = "127.0.0.1"  
        SOURCE_PORT = 51288
        
        DEST_IP = "127.0.0.1"   # Change this to match the AMF's NGAP Server IP
        DEST_PORT = 38412   # Change this to match the AMF's NGAP Server Port
    ```

    3.2) Now, in another terminal, execute the following command:

    ```sh
    python3 send_ng_setup_req.py
    ```