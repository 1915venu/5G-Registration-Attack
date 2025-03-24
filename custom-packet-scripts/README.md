# Triggering Authentication inside Core Network using custom NGAP Packets

This part of the repository contains code that can be used to send customized NGAP and RRC messages. It leverages [pycrate](https://github.com/pycrate-org/pycrate) and [pysctp](https://github.com/P1sec/pysctp) libraries of python to achieve this functionality.

## How to setup this Project?

> <u>**Pre-requisites:**</u>

- Pip3 and Python3.5 _(or, greater)_ installed on your system. For this setup, we will use Python 3.10.12.

- A successfully running core network simulator (e.g. Open5GS), already set-up on your host machine. For IITD students, please refer [here](https://github.com/spring-iitd/Cellular-Security) for simulator setup.

1. To clone this repository into the `~/shared/` directory, run the following commands:

```sh
cd ~/shared/
git clone https://github.com/spring-iitd/5G-Registration-Attack.git
```

2. Move into the appropriate folder and create a Python Virtual Environment as:

```sh
cd 5G-Registration-Attack/custom-packet-scripts/
sudo apt install python3.10-venv
python3 -m venv py_3.10.12
source py_3.10.12/bin/activate
```

3. Install the required dependencies for this project as:

```sh
pip3 install -r requirements.txt
```

4. Install [CryptoMobile](https://github.com/mitshell/CryptoMobile) toolkit as:

```sh
git clone https://github.com/mitshell/CryptoMobile.git
cd CryptoMobile
sudo apt install python3.10-dev
python3 setup.py install
cd ../
```

## Usage

Once the project is set up, you can use the various scripts provided to perform your simulations.

- e.g. Set up the correct source and destination IP and Port in the `5G-Registration-Attack/custom-packet-scripts/procedures/trigger_auth.py` in the following part of the code:

```py
def setup_sctp_connection():
    SOURCE_IP = "192.168.56.100"    # Script IP
    SOURCE_PORT = 51288             # Script Port

    DEST_IP = "192.168.56.3"        # AMF IP
    DEST_PORT = 9001                # AMF Port
```

- <u>_Note-1:_</u> Ensure that your source and destination IP belong to the same interface. You can manually assign an additional IP to an existing interface as:

```sh
sudo ip addr add 192.168.56.100/24 dev eth1
```

- <u>_Note-2:_</u> Ensure that your `AMF` is configured to receive `NGA`P`messages over`SCTP` at the specified port, as shown below:

```
amf:
  sbi:
    server:
      - address: 127.0.0.5
        port: 7777
    client:
#      nrf:
#        - uri: http://127.0.0.10:7777
      scp:
        - uri: http://127.0.0.200:7777
  ngap:
    server:
      - address: 192.168.56.3
        port: 9001              # Ensure that this port is explicitly, if unspecified
```

- Finally, you can execute the scripts as:

```sh
cd procedures
python3 trigger_auth.py
```

## Author & Contributors

- Prateek Bhaisora _(2023JCS2564)_
- IIT Delhi: ([spring-iitd](https://github.com/spring-iitd))
- GitHub: [prateekbhaisora](https://github.com/prateekbhaisora)
