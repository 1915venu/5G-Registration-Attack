from nas_utils.constants import *

def modify_fgmm_req_nas_pdu(fgmm_reg_req_nas_pdu):
    fgmm_reg_req_nas_pdu['5GMMHeader']['EPD'].set_val(126)
    fgmm_reg_req_nas_pdu['5GMMHeader']['spare'].set_val(0)
    fgmm_reg_req_nas_pdu['5GMMHeader']['SecHdr'].set_val(0)
    fgmm_reg_req_nas_pdu['5GMMHeader']['Type'].set_val(65)
    
    # print("debug\n")
    # print(fgmm_reg_req_nas_pdu['NAS_KSI']._IE_stat)
    # print(fgmm_reg_req_nas_pdu['NAS_KSI']._IE)
    # print("\n")
    
    # print(encode_bcd('0000000001'))
    
    fgmm_reg_req_nas_pdu['5GSRegType'].set_IE(val={'FOR': 1, 'Value': 1})
    fgmm_reg_req_nas_pdu['NAS_KSI'].set_IE(val={'TSC': 0, 'Value': 7})
    fgmm_reg_req_nas_pdu['5GSID']['L'].set_val(53)
    fgmm_reg_req_nas_pdu['5GSID'].set_IE(val= {'spare': 0, 'Fmt': 0, 'Type': 1, 'Value': {
            'PLMN': bytes.fromhex(PLMN),
            'RoutingInd': Routing_Indicator,
            'spare': 0,
            'ProtSchemeID': Protection_Scheme_ID,
            'HNPKID': Home_nw_public_key_ID,
            'Output': {
                'ECCEphemPK': bytes.fromhex(ECC_Ephemeral_public_key),
                'CipherText': bytes.fromhex(Ciphertext),
                'MAC': bytes.fromhex(MAC)
            }
        }
    })
    
    # print("debug\n")
    # print(fgmm_reg_req_nas_pdu._opts)
    # print("\n")
    
    fgmm_reg_req_nas_pdu['UESecCap'].set_trans(False)
    
    fgmm_reg_req_nas_pdu['UESecCap']['T'].set_val(46)
    fgmm_reg_req_nas_pdu['UESecCap']['L'].set_val(4)    
    fgmm_reg_req_nas_pdu['UESecCap'].set_IE(val={
        '5G-EA0': 1, '5G-EA1_128': 1, '5G-EA2_128': 1, '5G-EA3_128': 1,
        '5G-EA4': 0, '5G-EA5': 0, '5G-EA6': 0, '5G-EA7': 0,
        '5G-IA0': 1, '5G-IA1_128': 1, '5G-IA2_128': 1, '5G-IA3_128': 1,
        '5G-IA4': 0, '5G-IA5': 0, '5G-IA6': 0, '5G-IA7': 0,
        'EEA0': 1, 'EEA1_128': 1, 'EEA2_128': 1, 'EEA3_128': 1,
        'EEA4': 0, 'EEA5': 0, 'EEA6': 0, 'EEA7': 0,
        'EIA0': 1, 'EIA1_128': 1, 'EIA2_128': 1, 'EIA3_128': 1,
        'EIA4': 0, 'EIA5': 0, 'EIA6': 0, 'EIA7': 0
    }) 