#!/bin/bash

nr-gnb -c /home/vagrant/shared/ueransim/gnb130.yaml & 
sudo nr-ue -c /home/vagrant/shared/ueransim/ue130.yaml -n 100 -t 1500 &