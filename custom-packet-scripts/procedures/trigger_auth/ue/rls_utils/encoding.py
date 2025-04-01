from rls_utils.constants import RLS_MSG_TYPE_NAME, RLS_MSG_TYPE_VAL

def encode_rls_msg(msg_type_name, sti, rrc_msg=None):
    stream = bytearray()
    
    stream.append(0x03)
    
    stream.append(3)        
    stream.append(2)        
    stream.append(6)        
                
    msg_type_val = RLS_MSG_TYPE_VAL[msg_type_name]            
                
    stream.append(msg_type_val)
    stream.extend(sti.to_bytes(8, byteorder='big'))   

    if (msg_type_val == RLS_MSG_TYPE_VAL[RLS_MSG_TYPE_NAME["heartbeat"]]):
        simPosX = 0
        stream.extend(simPosX.to_bytes(4, byteorder='big'))
        simPosY = 0
        stream.extend(simPosY.to_bytes(4, byteorder='big'))
        simPosZ = 0
        stream.extend(simPosZ.to_bytes(4, byteorder='big'))

    elif (msg_type_val == RLS_MSG_TYPE_VAL[RLS_MSG_TYPE_NAME["rrc_pdu"]]):
        stream.append(1)
        pduID = 0 
        stream.extend(pduID.to_bytes(4, byteorder='big'))
        
        rrc_msg_type = None
        if msg_type_name == RLS_MSG_TYPE_NAME["rrc_setup_req"]:
            rrc_msg_type = 5
        elif msg_type_name == RLS_MSG_TYPE_NAME["rrc_reg_req"]:
            rrc_msg_type = 7
        if rrc_msg_type is None:
            raise ValueError(f"Unable to decide a RRC Message Type!")
        
        stream.extend(rrc_msg_type.to_bytes(4, byteorder='big'))
        pdu_len = len(rrc_msg)
        stream.extend(pdu_len.to_bytes(4, byteorder='big'))
        stream.extend(rrc_msg)
    
    return bytes(stream)