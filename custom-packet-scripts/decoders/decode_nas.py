from pycrate_mobile.NAS import *

hex_data = "7e00417900350199f90700000101f65e929e1b4851b7d5681cd3764bad551bc6d92ced536e2d73395decbe3d2933c351b27b393f4038c4497b0db42e04f0f0f0f02f020101"

Msg, err = parse_NAS_MO(unhexlify(hex_data))

print(f"{show(Msg)}\n")
print(f"{show(Msg['NSSAI']['NSSAI'][0]['Len'])}\n")

print(f"{dir(Msg)}\n")

if Msg:
    print("\nEPD:", Msg.get_val() if hasattr(Msg, 'get_val') else "Not Available")
    print("\n")
    print("Security Header Type:", Msg.get_header() if hasattr(Msg, 'get_header') else "Not Available")
    print("\n")
    
else:
    print("Failed to parse NAS message!\n")
    
print(Msg.to_json())
