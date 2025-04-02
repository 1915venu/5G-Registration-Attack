# Triggering Authentication inside Core Network using custom NGAP Packets

This part of the repository contains code that can be used to send customized `NGAP` messages, thereby mimicking a `gNB + UE`, to trigger authentication inside the core network. It leverages [pycrate](https://github.com/pycrate-org/pycrate) and [pysctp](https://github.com/P1sec/pysctp) libraries of python to achieve this functionality.

## Setup Instructions

- For installation and setup, please refer to the [main](../README.md) README file. 

## Usage

1. Set up the correct source and destination IP and Port in the `./procedures/trigger_auth/gnb/shared_utils/constants.py` in the following part of the code:

```py
SRC_IP = "192.168.58.100"   # Script IP
SRC_PORT = 51288            # Script Port

DST_IP = "192.168.58.100"   # AMF's NGAP IP
DST_PORT = 9001             # AMF's NGAP Port 
```

- <u>_Note-1:_</u> Ensure that your source and destination IP belong to the same interface. You can manually assign an additional IP to an existing interface as:

```sh
sudo ip addr add 192.168.56.100/24 dev eth1
```

  - <u>_Note-2:_</u> Ensure that your `AMF` is configured to receive `NGAP` messages over`SCTP` at the specified IP and port, in your core network's `amf.yaml` file as shown below:

```sh
amf:
  sbi:
    server:
      - address: amf1.localdomain
        port: 80
    client:
      # nrf:
      #   - uri: http://nrf.localdomain:80
      scp:
        - uri: http://scp.localdomain:80
  ngap:
    server:
      - address: 192.168.58.100
        port: 9001  # Ensure that this port is added explicitly, if unspecified
```

3. Finally, you can execute the scripts as:

```sh
cd procedures/trigger_auth/gnb/
python3 main.py
```

## Author & Contributors

> Prateek Bhaisora _(2023JCS2564)_ <br>
IIT Delhi SPRING Group ([spring-iitd](https://github.com/spring-iitd)) <br>
GitHub Profile Link: [prateekbhaisora](https://github.com/prateekbhaisora)