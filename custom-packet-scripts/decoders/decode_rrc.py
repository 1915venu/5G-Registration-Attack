import binascii
from pycrate_asn1dir import RRCNR

hex_data = "3000080000"
packet_bytes = binascii.unhexlify(hex_data)

print(f"{packet_bytes}\n")

rrc_msg = RRCNR.NR_RRC_Definitions.DL_CCCH_Message

rrc_msg.from_uper(packet_bytes)

print(f"{rrc_msg.get_val()}\n")