import random
from rrc_utils.constants import MAX_UE_ID

def modify_rrc_setup_req(rrc_setup_req):
    # print(rrc_setup_req.get_proto())
 
    random_value = 0
    while True:
        random_value = random.randint(10**11, MAX_UE_ID)
        if random_value <= MAX_UE_ID:  
            break
    # print(f"RandomValue: {random_value}") 
    
    pdu_data = {'message': ('c1', ('rrcSetupRequest', {'rrcSetupRequest': {'ue-Identity': ('randomValue', (random_value, 39)), 'establishmentCause': 'mo-Signalling', 'spare': (1, 1)}}))}

    rrc_setup_req.set_val(pdu_data)
    # print(rrc_setup_req.to_asn1())
    
def modify_nas_pdu(nas_pdu):
    nas_pdu['5GMMHeader']['EPD'].set_val(126)
    nas_pdu['5GMMHeader']['spare'].set_val(0)
    nas_pdu['5GMMHeader']['SecHdr'].set_val(0)
    nas_pdu['5GMMHeader']['Type'].set_val(65)
    
    # print("Debug:\n")
    # print(nas_pdu['NAS_KSI']._IE_stat)
    # print(nas_pdu['NAS_KSI']._IE)
    # print("\n")
    
    nas_pdu['NAS_KSI'].set_IE(val={'TSC': 0, 'Value': 7})
    nas_pdu['5GSRegType'].set_IE(val={'FOR': 1, 'Value': 1})
    nas_pdu['5GSID']['L'].set_val(53)
    nas_pdu['5GSID'].set_IE(val= {'spare': 0, 'Fmt': 0, 'Type': 1, 'Value': {
            'PLMN': bytes.fromhex('99f907'),
            'RoutingInd': '0000',
            'spare': 0,
            'ProtSchemeID': 1,
            'HNPKID': 1,
            'Output': {
                'ECCEphemPK': bytes.fromhex('f65e929e1b4851b7d5681cd3764bad551bc6d92ced536e2d73395decbe3d2933'),
                'CipherText': bytes.fromhex('c351b27b39'),
                'MAC': bytes.fromhex('3f4038c4497b0db4')
            }
        }
    })
    
    # print("Debug:\n")
    # print(nas_pdu._opts)
    # print("\n")
    
    nas_pdu['UESecCap'].set_trans(False)
    nas_pdu['UESecCap']['T'].set_val(46)
    nas_pdu['UESecCap']['L'].set_val(4)    
    nas_pdu['UESecCap'].set_IE(val={
        '5G-EA0': 1, '5G-EA1_128': 1, '5G-EA2_128': 1, '5G-EA3_128': 1,
        '5G-EA4': 0, '5G-EA5': 0, '5G-EA6': 0, '5G-EA7': 0,
        '5G-IA0': 1, '5G-IA1_128': 1, '5G-IA2_128': 1, '5G-IA3_128': 1,
        '5G-IA4': 0, '5G-IA5': 0, '5G-IA6': 0, '5G-IA7': 0,
        'EEA0': 1, 'EEA1_128': 1, 'EEA2_128': 1, 'EEA3_128': 1,
        'EEA4': 0, 'EEA5': 0, 'EEA6': 0, 'EEA7': 0,
        'EIA0': 1, 'EIA1_128': 1, 'EIA2_128': 1, 'EIA3_128': 1,
        'EIA4': 0, 'EIA5': 0, 'EIA6': 0, 'EIA7': 0
    })
    
    nas_pdu['NSSAI'].set_trans(False)
    nas_pdu['NSSAI']['T'].set_val(47)
    nas_pdu['NSSAI']['L'].set_val(2)
    nas_pdu['NSSAI'].set_IE(val=[
        {  
            'Len': 1,
            'SNSSAI': {
                'SST': 1
            }
        }
    ])
    
def modify_rrc_reg_req(rrc_reg_req, reg_nas_pdu, rrc_transaction_id):
    # print(rrc_reg_req.get_proto())
    
    pdu_data = {'message': ('c1', ('rrcSetupComplete', {'rrc-TransactionIdentifier': rrc_transaction_id, 'criticalExtensions': ('rrcSetupComplete', {'selectedPLMN-Identity': 1, 'dedicatedNAS-Message': reg_nas_pdu})}))}

    rrc_reg_req.set_val(pdu_data)
    
    # print(rrc_reg_req.to_asn1()) 