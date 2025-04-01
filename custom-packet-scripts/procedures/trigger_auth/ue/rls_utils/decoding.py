import copy
from shared_utils.constants import SEPARATOR
from rrc_utils.decoding import decode_rrc_msg
from rrc_utils.constants import RRC_MSG_TYPE_VAL
from rls_utils.constants import RLS_MSG_TYPE_NAME, RLS_MSG_TYPE_VAL 
from rls_utils.constants import HEADER_VAL, UERANSIM_MAJOR_VERSION, UERANSIM_MINOR_VERSION, UERANSIM_PATCH_NUMBER

def decode_rls_msg(gnb_res, debug=True):
    stream = bytearray(gnb_res)
    index = 0  
    
    old_header_val = stream[index]
    if (old_header_val != HEADER_VAL):
        print(SEPARATOR)
        raise ValueError(f"RLS Message breaks backward compatibility!")
    
    if (debug):
        print(f"Old header value (for backward compatibility): {old_header_val}")
    index += 1

    major_version_number = stream[index]
    if (major_version_number != UERANSIM_MAJOR_VERSION):
        print(SEPARATOR)
        raise ValueError(f"UERANSIM Major Version Mismatch!")
    
    minor_version_number = stream[index + 1]
    if (minor_version_number != UERANSIM_MINOR_VERSION):
        print(SEPARATOR)
        raise ValueError(f"UERANSIM Minor Version Mismatch!")
    
    patch_number = stream[index + 2]
    if (patch_number != UERANSIM_PATCH_NUMBER):
        print(SEPARATOR)
        raise ValueError(f"UERANSIM Patch Number Mismatch!")
    
    if (debug):
        print(f"UERANSIM Version: {major_version_number}.{minor_version_number}.{patch_number}")
    index += 3
    
    msg_type_val = stream[index]
    index += 1
    
    sti = int.from_bytes(stream[index:index+8], byteorder='big')
    index += 8

    if (debug):
        print(f"Message Type is: {msg_type_val}")
        print(f"Sender Node Temporary ID is: {sti}")

    if msg_type_val == RLS_MSG_TYPE_VAL[RLS_MSG_TYPE_NAME["heartbeat_ack"]]:
        rls_signal_strength = int.from_bytes(stream[index:index+4], byteorder='big')
        if (debug):
            print(f"RLS Signal Strength is: {rls_signal_strength}")
        index += 4

    elif msg_type_val == RLS_MSG_TYPE_VAL[RLS_MSG_TYPE_NAME["rrc_pdu"]]:
        pdu_type = stream[index] 
        if (pdu_type != 1):
            print(SEPARATOR)
            raise ValueError(f"PDU Type doesn't match a RRC Message!") 
        if (debug):
            print(f"PDU Type is: {pdu_type}")
        index += 1
        
        pdu_ID = int.from_bytes(stream[index:index+4], byteorder='big')
        if (debug):
            print(f"PDU ID is: {pdu_ID}")
        index += 4
        
        rrc_msg_type = int.from_bytes(stream[index:index+4], byteorder='big')
        # print(f"RRC Message type received is: {rrc_msg_type}\n")
        
        if (rrc_msg_type == RRC_MSG_TYPE_VAL["BCCH-BCH"] or rrc_msg_type == RRC_MSG_TYPE_VAL["BCCH-DL-SCH"]):
            print("\nIgnoring MIB and/or SIB1 Broadcasts!")
            return None
        
        elif (rrc_msg_type != RRC_MSG_TYPE_VAL["DL-DCCH"] and rrc_msg_type != RRC_MSG_TYPE_VAL["DL-CCCH"]):
            print(SEPARATOR)
            raise ValueError(f"RRC Message Type doesn't match a DL-DCCH or, a DL-CCCH Message!") 
        index += 4
        
        pdu_len = int.from_bytes(stream[index:index+4], byteorder='big')
        if (debug):
            print(f"PDU Length is: {pdu_len}")
        index += 4

    return gnb_res[index:]

def parse_gnb_response(gnb_res, msgTypeName):
    print(SEPARATOR)
    # print("Received GNB Response: ", gnb_res.hex())
            
    print(f"Recieved {msgTypeName}:\n")    
    gnb_res = decode_rls_msg(gnb_res)
        
    msg_type_val = RLS_MSG_TYPE_VAL[msgTypeName]
        
    if msg_type_val == RLS_MSG_TYPE_VAL[RLS_MSG_TYPE_NAME["heartbeat_ack"]]:
        return None
    elif msg_type_val == RLS_MSG_TYPE_VAL[RLS_MSG_TYPE_NAME["rrc_pdu"]]:
        return decode_rrc_msg(gnb_res, msgTypeName)
    
    return None

def check_mib_or_sib1(gnb_res_original):
    
    gnb_res_copy = copy.deepcopy(gnb_res_original)
    mib_sib1_indicator = decode_rls_msg(gnb_res_copy, False)
    
    if mib_sib1_indicator is None:
        return None
    
    return gnb_res_original