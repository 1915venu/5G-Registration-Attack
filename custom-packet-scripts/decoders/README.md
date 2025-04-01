# Custom Decoders

This part of the repository contains decoders that leverages objects and methods, provided by [pycrate](https://github.com/pycrate-org/pycrate) to decode `NGAP`, `NAS`, `RRC` and `SCTP` messages. These decoders were primarily used for debugging purposes, during the development of this project.   

## Setup Instructions

- For installation and setup, please refer to the [main](../README.md) README file. 

## Usage

1. Provide a hex or byte representation of packets (e.g., copying captured packets from a PCAP file as a hex stream) and assign the values to the respective variables. 
e.g.  
Suppose you want to decode a `RRC` message using `decode_rrc.py`:  


```sh
hex_data = "3000080000" # Replace with a similar hex stream
packet_bytes = b'0\x00\x08\x00\x00' # Replace with a similar byte stream
```

2. Run the Python script to decode the message using the following command:
  
```sh
python3 decode_rrc.py
```