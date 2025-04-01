import binascii
from pycrate_asn1dir.NGAP import *

raw_bytes = b' \x15\x002\x00\x00\x04\x00\x01\x00\x0e\x05\x80open5gs-amf1\x00`\x00\x08\x00\x00\x99\xf9\x07\x01\x00@\x00V@\x01\xff\x00P\x00\x08\x00\x99\xf9\x07\x00\x00\x00\x08'
hex_data = raw_bytes.hex()
# hex_data = "000f407000000500550002000100260042417e00417900350199f90700000101f65e929e1b4851b7d5681cd3764bad551bc6d92ced536e2d73395decbe3d2933c351b27b393f4038c4497b0db42e04f0f0f0f0007900135099f907000000010099f907000001eb867b68005a4001180070400100"

packet_bytes = bytes.fromhex(hex_data)

ngap_pdu = NGAP_PDU_Descriptions.NGAP_PDU

ngap_pdu.from_aper(binascii.unhexlify(hex_data))

print(f"{ngap_pdu.to_asn1()}\n")

ngap_pdu.from_aper(packet_bytes)

print(f"{ngap_pdu.get_val()}\n")