#!/bin/bash
#Bring up the VMs 
vagrant up 
#Start the open5gs core
vagrant ssh open5gs -c 'nohup bash /home/vagrant/shared/core_config1.sh > open5gs.log & sleep 1'
sleep 5

#declare -a units=("0", "25", "50", "100", "200", "400")

#start packet-capture for filter NGAP 
tshark -i bridge102 -f 'port 38412' -w ngap_captured_traffic_.pcap &
TSHARK_PID=$!

vagrant ssh rusher_box1 -c 'nohup /home/vagrant/PacketRusher/packetrusher --config /home/vagrant/shared/packetrusher/config0.yml multi-ue-pdu --number-of-ues 25 --timeBetweenRegistration 100 --numPduSessions 1 --loop > rusher1.log 2>&1 & sleep 1'

vagrant ssh rusher_box1 -c 'nohup /home/vagrant/PacketRusher/packetrusher --config /home/vagrant/shared/packetrusher/config1.yml multi-ue-pdu --number-of-ues 25 --timeBetweenRegistration 100 --numPduSessions 1 --loop > rusher2.log 2>&1 & sleep 1'

vagrant ssh rusher_box1 -c 'nohup /home/vagrant/PacketRusher/packetrusher --config /home/vagrant/shared/packetrusher/config2.yml multi-ue-pdu --number-of-ues 25 --timeBetweenRegistration 100 --numPduSessions 1 --loop > rusher3.log 2>&1 & sleep 1'

vagrant ssh rusher_box2 -c 'nohup /home/vagrant/PacketRusher/packetrusher --config /home/vagrant/shared/packetrusher/config3.yml multi-ue-pdu --number-of-ues 25 --timeBetweenRegistration 100 --numPduSessions 1 --loop > rusher4.log 2>&1 & sleep 1'

vagrant ssh rusher_box2 -c 'nohup /home/vagrant/PacketRusher/packetrusher --config /home/vagrant/shared/packetrusher/config4.yml multi-ue-pdu --number-of-ues 25 --timeBetweenRegistration 100 --numPduSessions 1 --loop > rusher5.log 2>&1 & sleep 1'

vagrant ssh rusher_box2 -c 'nohup /home/vagrant/PacketRusher/packetrusher --config /home/vagrant/shared/packetrusher/config5.yml multi-ue-pdu --number-of-ues 25 --timeBetweenRegistration 100 --numPduSessions 1 --loop > rusher6.log 2>&1 & sleep 1'

vagrant ssh ue_box1 -c 'sudo nohup nr-gnb -c /home/vagrant/shared/ueransim/gnb0.yaml > gnb0.log & sleep 1'

vagrant ssh ue_box1 -c 'sudo nohup nr-ue -c /home/vagrant/shared/ueransim/ue0.yaml -n 75 -t 1500 & > ue0.log & sleep 1'

sleep 90

sudo kill -SIGKILL $TSHARK_PID

tshark -i bridge102 -i bridge100 -w bridge3_bridge6.pcap duration:30 &
TSHARK_PID=$!

vagrant ssh rusher_box1 -c 'nohup iperf3 -s -D > iperf_server.log & sleep 1'

vagrant ssh ue_box1 -c 'nohup  nr-binder 10.45.0.3 iperf3 -c 10.211.55.225 -u -b 50M > iperf_client.log & sleep 1'

sudo kill -SIGKILL $TSHARK_PID
#stop the open5gs core

