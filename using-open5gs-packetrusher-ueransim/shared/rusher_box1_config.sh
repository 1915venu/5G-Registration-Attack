/home/vagrant/PacketRusher/packetrusher --config /home/vagrant/shared/packetrusher/config0.yml multi-ue-pdu --number-of-ues 50 --timeBetweenRegistration 100 --numPduSessions 1 --loop > rusher0.log &

/home/vagrant/PacketRusher/packetrusher --config /home/vagrant/shared/packetrusher/config1.yml multi-ue-pdu --number-of-ues 50 --timeBetweenRegistration 100 --numPduSessions 1 --loop > rusher1.log &

/home/vagrant/PacketRusher/packetrusher --config /home/vagrant/shared/packetrusher/config2.yml multi-ue-pdu --number-of-ues 50 --timeBetweenRegistration 100 --numPduSessions 1 --loop > rusher2.log &