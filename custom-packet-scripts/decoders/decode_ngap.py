from pycrate_asn1dir.NGAP import *

raw_bytes = b' \x15\x002\x00\x00\x04\x00\x01\x00\x0e\x05\x80open5gs-amf1\x00`\x00\x08\x00\x00\x99\xf9\x07\x01\x00@\x00V@\x01\xff\x00P\x00\x08\x00\x99\xf9\x07\x00\x00\x00\x08'
hex_data = raw_bytes.hex()
# hex_data = "00150043000004001b00090099f9075000000001005240170a00554552414e53494d2d676e622d3939392d37302d310066000f00000000010099f907000100080080001540014000"

packet_bytes = bytes.fromhex(hex_data)

ngap_pdu = NGAP_PDU_Descriptions.NGAP_PDU

ngap_pdu.from_aper_ws(packet_bytes)

print(ngap_pdu.get_val())