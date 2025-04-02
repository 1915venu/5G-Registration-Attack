# Triggering Authentication inside Core Network using custom RRC Packets

This part of the repository contains code that can be used to send customized `NGAP` messages, thereby mimicking a `gNB + UE`, to trigger authentication inside the core network. It leverages [pycrate](https://github.com/pycrate-org/pycrate) library of python to achieve this functionality.

## Setup Instructions

- For installation and setup, please refer to the [main](../README.md) README file. 

## Usage

1. Set up the correct source and destination IP and Port in the `./procedures/trigger_auth/ue/shared_utils/constants.py` in the following part of the code:

```py
SRC_UE_IP = "192.168.58.101"    # Script IP    
SRC_UE_PORT = 55863             # Script IP

DST_GNB_IP = "192.168.58.101"   # gNB's RLS IP
DST_GNB_PORT = 4997             # gNB's RLS Port
```

- <u>_Note-1:_</u> Ensure that your source and destination IP belong to the same interface. You can manually assign an additional IP to an existing interface as:

```sh
sudo ip addr add 192.168.58.101/24 dev eth1
```

  - <u>_Note-2:_</u> Ensure that your `gNB` is configured to receive `RLS` messages over`UDP` at the specified IP, in your RAN network's `gnb.yaml` file as shown below:

```sh
linkIp: 192.168.58.101  # gNB's local IP address for Radio Link Simulation (Usually same with local IP) -> Replace with correct IP here.
ngapIp: 192.168.58.101  # gNB's local IP address for N2 Interface (Usually same with local IP)
gtpIp: 192.168.58.101   # gNB's local IP address for N3 Interface (Usually same with local IP)
```

1. Finally, you can execute the scripts as:

```sh
cd procedures/trigger_auth/ue/
python3 main.py
```

## Author & Contributors

> Prateek Bhaisora _(2023JCS2564)_ <br>
IIT Delhi SPRING Group ([spring-iitd](https://github.com/spring-iitd)) <br>
GitHub Profile Link: [prateekbhaisora](https://github.com/prateekbhaisora)
