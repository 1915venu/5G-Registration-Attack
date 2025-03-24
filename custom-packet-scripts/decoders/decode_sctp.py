import struct
import json
from pycrate_asn1dir.NGAP import *

hex_data = "00150043000004001b00090099f9075000000001005240170a00554552414e53494d2d676e622d3939392d37302d310066000f00000000010099f9070001000800800015400140"

raw_bytes = bytes.fromhex(hex_data)

sctp_header = struct.unpack("!HHII", raw_bytes[:12])

sctp_info = {
    "source_port": sctp_header[0],
    "destination_port": sctp_header[1],
    "verification_tag": sctp_header[2],
    "checksum": hex(sctp_header[3]),
}

ngap_bytes = raw_bytes[12:]

print(ngap_bytes.hex())

ngap_pdu = NGAP_PDU_Descriptions.NGAP_PDU

ngap_pdu.from_aper_ws(ngap_bytes)

print(ngap_pdu.get_val())

decoded_data = {
    "sctp": sctp_info,
    "ngap_decoded": json.loads(ngap_pdu.get_val())
}

json_result = json.dumps(decoded_data, indent=4)

print(json_result)