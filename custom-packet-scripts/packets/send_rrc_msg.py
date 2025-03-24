import socket
from pycrate_asn1dir import RRCLTE

def modify_rrc_msg(rrc_msg):
    
    # print(dir(rrc_msg))
    # print(rrc_msg.get_proto())
    
    json_str = """
    {
        "message": {
            "c1": {
                "systemInformation": {
                    "criticalExtensions": {
                        "systemInformation-r8": {
                            "sib-TypeAndInfo": [
                                {
                                    "sib2": {
                                        "ac-BarringInfo": {
                                            "ac-BarringForEmergency": false,
                                            "ac-BarringForMO-Data": {
                                                "ac-BarringFactor": "p95",
                                                "ac-BarringForSpecialAC": "00",
                                                "ac-BarringTime": "s8"
                                            },
                                            "ac-BarringForMO-Signalling": {
                                                "ac-BarringFactor": "p95",
                                                "ac-BarringForSpecialAC": "00",
                                                "ac-BarringTime": "s8"
                                            }
                                        },
                                        "freqInfo": {
                                            "additionalSpectrumEmission": 1,
                                            "ul-Bandwidth": "n100",
                                            "ul-CarrierFreq": 19400
                                        },
                                        "radioResourceConfigCommon": {
                                            "bcch-Config": { "modificationPeriodCoeff": "n8" },
                                            "pcch-Config": { "defaultPagingCycle": "rf64", "nB": "quarterT" },
                                            "pdsch-ConfigCommon": { "p-b": 1, "referenceSignalPower": 8 },
                                            "prach-Config": {
                                                "prach-ConfigInfo": {
                                                    "highSpeedFlag": false,
                                                    "prach-ConfigIndex": 3,
                                                    "prach-FreqOffset": 4,
                                                    "zeroCorrelationZoneConfig": 12
                                                },
                                                "rootSequenceIndex": 12
                                            },
                                            "pucch-ConfigCommon": {
                                                "deltaPUCCH-Shift": "ds2",
                                                "n1PUCCH-AN": 36,
                                                "nCS-AN": 0,
                                                "nRB-CQI": 4
                                            },
                                            "pusch-ConfigCommon": {
                                                "pusch-ConfigBasic": {
                                                    "enable64QAM": false,
                                                    "hoppingMode": "interSubFrame",
                                                    "n-SB": 1,
                                                    "pusch-HoppingOffset": 6
                                                },
                                                "ul-ReferenceSignalsPUSCH": {
                                                    "cyclicShift": 0,
                                                    "groupAssignmentPUSCH": 0,
                                                    "groupHoppingEnabled": false,
                                                    "sequenceHoppingEnabled": false
                                                }
                                            },
                                            "rach-ConfigCommon": {
                                                "maxHARQ-Msg3Tx": 5,
                                                "powerRampingParameters": {
                                                    "powerRampingStep": "dB2",
                                                    "preambleInitialReceivedTargetPower": "dBm-96"
                                                },
                                                "preambleInfo": {
                                                    "numberOfRA-Preambles": "n40",
                                                    "preamblesGroupAConfig": {
                                                        "messagePowerOffsetGroupB": "dB10",
                                                        "messageSizeGroupA": "b144",
                                                        "sizeOfRA-PreamblesGroupA": "n32"
                                                    }
                                                },
                                                "ra-SupervisionInfo": {
                                                    "mac-ContentionResolutionTimer": "sf64",
                                                    "preambleTransMax": "n10",
                                                    "ra-ResponseWindowSize": "sf10"
                                                }
                                            },
                                            "soundingRS-UL-ConfigCommon": { "release": null },
                                            "ul-CyclicPrefixLength": "len1",
                                            "uplinkPowerControlCommon": {
                                                "alpha": "al04",
                                                "deltaFList-PUCCH": {
                                                    "deltaF-PUCCH-Format1": "deltaF0",
                                                    "deltaF-PUCCH-Format1b": "deltaF1",
                                                    "deltaF-PUCCH-Format2": "deltaF0",
                                                    "deltaF-PUCCH-Format2a": "deltaF0",
                                                    "deltaF-PUCCH-Format2b": "deltaF0"
                                                },
                                                "deltaPreambleMsg3": 1,
                                                "p0-NominalPUCCH": -116,
                                                "p0-NominalPUSCH": -80
                                            }
                                        },
                                        "timeAlignmentTimerCommon": "sf10240",
                                        "ue-TimersAndConstants": {
                                            "n310": "n10",
                                            "n311": "n1",
                                            "t300": "ms400",
                                            "t301": "ms400",
                                            "t310": "ms2000",
                                            "t311": "ms3000"
                                        }
                                    }
                                }
                            ]
                        }
                    }
                }
            }
        }
    }
    """

    rrc_msg.from_jer(json_str)
    rrc_msg = rrc_msg.to_uper()

def send_rrc_msg(rrc_msg):
    UDP_IP = "192.168.58.101"  
    UDP_PORT = 4997 

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.sendto(rrc_msg, (UDP_IP, UDP_PORT))
    print(f"Sent rrc_msg to {UDP_IP}:{UDP_PORT}\n")

    sock.close()

def main():
    
    rrc_msg = RRCLTE.EUTRA_RRC_Definitions.BCCH_DL_SCH_Message

    modify_rrc_msg(rrc_msg)
    
    rrc_msg = rrc_msg.to_uper()
    
    send_rrc_msg(rrc_msg)

if __name__ == "__main__":
    main()