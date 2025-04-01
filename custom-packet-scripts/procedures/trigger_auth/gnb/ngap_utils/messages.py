import time
import struct
from ngap_utils.constants import *

def modify_ng_setup_req(ng_setup_req):
    # print(ng_setup_req.get_proto())
    
    IEs = []
        
    IEs.append({'id': 27, 'criticality': 'reject', 'value': ('GlobalRANNodeID', ('globalGNB-ID', {'pLMNIdentity': PLMN_Identity, 'gNB-ID': ('gNB-ID', (1, 32))}))})
    IEs.append({'id': 82, 'criticality': 'ignore', 'value': ('RANNodeName', RAN_Node_Name)})
    IEs.append({'id': 102, 'criticality': 'reject', 'value': ('SupportedTAList', [{'tAC': TAC, 'broadcastPLMNList': [{'pLMNIdentity': PLMN_Identity, 'tAISliceSupportList': [ {'s-NSSAI': {'sST': SST_1}}, {'s-NSSAI': {'sST': SST_2}} ]}]}])})
    IEs.append({'id': 21, 'criticality': 'ignore', 'value': ('PagingDRX', 'v128')})
    pdu_data = ('initiatingMessage', {'procedureCode': 21, 'criticality': 'reject', 'value': ('NGSetupRequest', {'protocolIEs': IEs})})
    
    ng_setup_req.set_val(pdu_data)
    # print(ng_setup_req.to_asn1())
    
def modify_init_ue_msg(init_ue_msg, fgmm_reg_req_nas_pdu):
    # print(init_ue_msg.get_proto())
    
    curTime = int(time.time()) + 2208988800
    
    IEs = []
    
    IEs.append({'id': 85, 'criticality': 'reject', 'value': ('RAN-UE-NGAP-ID', 1)})
    IEs.append({'id': 38, 'criticality': 'reject', 'value': ('NAS-PDU', fgmm_reg_req_nas_pdu)})
    IEs.append({'id': 121, 'criticality': 'reject', 'value': ('UserLocationInformation', ('userLocationInformationNR', {'nR-CGI': {'pLMNIdentity': PLMN_Identity, 'nRCellIdentity': (16, 36)}, 'tAI': {'pLMNIdentity': PLMN_Identity, 'tAC': TAC }, 'timeStamp': struct.pack("!I",curTime)}))})
    IEs.append({'id': 90, 'criticality': 'ignore', 'value': ('RRCEstablishmentCause', 'mo-Signalling')})
    IEs.append({'id': 112, 'criticality': 'ignore', 'value': ('UEContextRequest', 'requested')})
    pdu_data = ('initiatingMessage', {'procedureCode': 15, 'criticality': 'ignore', 'value': ('InitialUEMessage', {'protocolIEs': IEs})})
        
    init_ue_msg.set_val(pdu_data)