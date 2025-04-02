# Triggering Authentication inside Core Network using custom NGAP and/or RRC Packets

This part of the repository contains code that can be used to send customized NGAP and/or RRC messages, to trigger the Authentication procedure, inside the core network. It leverages [pycrate](https://github.com/pycrate-org/pycrate) and [pysctp](https://github.com/P1sec/pysctp) libraries of python to achieve this functionality.

# Directory Structure

- This directory contains two sub-directories:
  
    1. `./gnb/`: This contains code to trigger authentication procedure in the `core` network by sending custom `NGAP` packets, thereby simulating `gNB + UE`.

    2. `./ue/`: This contains code to trigger authentication procedure in the `core` network by sending custom `RRC` packets to the `gNB`, thereby simulating a `UE`.

    - <u>_Note:_</u> The `UE` part is compatible only with [UERANSIM](https://github.com/aligungr/UERANSIM) as of now, since it sends `RRC` messages, encapsulated inside `RLS` messages, which is a custom protocol used in `UERASIM` to simulate Radio Links.

- The `./gnb/` sub-directory consists of the following:

    1. `./gnb/nas_utils`: This contains code for encoding, decoding and modifying `NAS` messages in 5G NR.

    2. `./gnb/ngap_utils`: This contains code for encoding, decoding and modifying `NGAP` messages. 
   
    3. `./gnb/shared_utils`: This contains code for some common variables and data structures, to implement `./gnb/main.py`.
   
    4. `./gnb/main.py`: This contains the `main()` used to invoke the authentication procedure in 5G core network.
   
    5. `./gnb/README.md`: This contains the documentation for setting up and usage of the above code.

- The `./ue/` sub-directory consists of the following:

    1. `./ue/rls_utils`: This contains code for encoding, decoding and modifying `RLS` messages in `UERANSIM`.

    2. `./ue/rrc_utils`: This contains code for encoding, decoding and modifying `RRC` messages. 
   
    3. `./ue/shared_utils`: This contains code for some common variables and data structures, to implement `./ue/main.py`.
   
    4. `./ue/main.py`: This contains the `main()` used to invoke the authentication procedure in 5G core network.
   
    5. `./ue/README.md`: This contains the documentation for setting up and usage of the above code.

## Author & Contributors

> Prateek Bhaisora _(2023JCS2564)_ <br>
IIT Delhi SPRING Group ([spring-iitd](https://github.com/spring-iitd)) <br>
GitHub Profile Link: [prateekbhaisora](https://github.com/prateekbhaisora)