import json
from binascii import unhexlify
from pycrate_mobile.NAS import *
from shared_utils.constants import SEPARATOR

def decode_nas(nas_pdu_bytes):
    hex_data = nas_pdu_bytes.hex()
    
    Msg, err = parse_NAS_MO(unhexlify(hex_data))
    
    if err:
        print(SEPARATOR)
        raise ValueError("Unable to decode NAS message!")
    
    return json.dumps(json.loads(Msg.to_json()), separators=(',', ':'))

def check_for_NAS(ngap_data):
    try:
        message_type, message_content = ngap_data
        if "protocolIEs" in message_content["value"][1]:  
            for ie in message_content["value"][1]["protocolIEs"]:
                if ie["id"] == 38:  
                    return ie["value"][1]  
    except Exception as e:
        print(SEPARATOR)
        print(f"Error extracting NAS-PDU: {e}")
        print(SEPARATOR)

    return None