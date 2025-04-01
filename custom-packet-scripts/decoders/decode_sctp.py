import struct
from pycrate_asn1dir.NGAP import *

hex_data = "232ab31c7e6b0e4c1806964c00030046c8e8078d000000000000003c"

raw_bytes = bytes.fromhex(hex_data)

sctp_header = struct.unpack("!HHII", raw_bytes[:12])

sctp_info = {
    "source_port": sctp_header[0],
    "destination_port": sctp_header[1],
    "verification_tag": sctp_header[2],
    "checksum": hex(sctp_header[3]),
}

print(f"{sctp_info}\n")