from pycrate_asn1dir import RRCNR
from rls_utils.constants import RLS_MSG_TYPE_NAME

def decode_rrc_msg(gnb_res, msg_type_name):
    rrc_msg = None
    if msg_type_name == RLS_MSG_TYPE_NAME["rrc_setup_res"]:
        rrc_msg = RRCNR.NR_RRC_Definitions.DL_CCCH_Message
    elif msg_type_name == RLS_MSG_TYPE_NAME["auth_req"]:
        rrc_msg = RRCNR.NR_RRC_Definitions.DL_DCCH_Message
    rrc_msg.from_uper(gnb_res)
    
    rrc_transaction_id = rrc_msg.get_val()['message'][1][1]['rrc-TransactionIdentifier']
    # print(f"\nRetrieved Transaction ID is: {rrc_transaction_id}\n")
    # print(rrc_msg.get_val())
    return rrc_transaction_id