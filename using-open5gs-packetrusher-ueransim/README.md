# Experiment Attack Scenario 1 
## Description
This attack scenario is a simple attack scenario where the attacker will be sending a high frequency of attach requests to the open5gs core network. The attack will be performed using the PacketRusher tool. While the polling on how long it is taking for registration is done using UERANSIM.

The attack scenario is as follows:
- The attacker will be running on rusher_box1 and rusher_box2
- The attacker will be sending a high frequency of attach requests to the open5gs core network
``` 
/home/vagrant/PacketRusher/packetrusher \
--config /home/vagrant/shared/packetrusher/config.yml  \
multi-ue-pdu --number-of-ues 10  \
--timeBetweenRegistration 100 \
--numPduSessions 1 \
--loop 
```

## Experiment Setup
The experiment setup is as follows:
- (RAM:1GB, CPU:1) open5gs-box is a VM that runs the open5gs core network 
- (RAM:2GB, CPU:2) rusher_box1 has three network interfaces all of which will be used for the attack
- (RAM:2GB, CPU:2) rusher_box2 has three network interfaces all of which will be used for the attack
- (RAM:2GB, CPU:2) ue_box1 is a VM that runs the UE, and will be polling at a low frequency

## Experiment 