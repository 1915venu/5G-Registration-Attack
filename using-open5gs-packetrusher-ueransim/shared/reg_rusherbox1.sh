#!/bin/bash

nr-gnb -c /home/vagrant/shared/ueransim/gnb0.yaml &
nr-gnb -c /home/vagrant/shared/ueransim/gnb1.yaml &
nr-gnb -c /home/vagrant/shared/ueransim/gnb2.yaml &

supi0=999700000000200
supi1=999700000001876
supi2=999700000003551

#----#----#----#----#----#----#----#----#----#----#----#----#----#----#----#----#----#----#----#----#----

sudo nr-ue -c /home/vagrant/shared/ueransim/ue0.yaml -i $supi0 -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $supi1 -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $supi2 -n 400 -t 25 &
sleep 10

sudo nr-ue -c /home/vagrant/shared/ueransim/ue0.yaml -i $((supi0+400)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+400)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+400)) -n 400 -t 25 &
sleep 10

sudo nr-ue -c /home/vagrant/shared/ueransim/ue0.yaml -i $((supi0+800)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+800)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+800)) -n 400 -t 25 &
sleep 10

sudo nr-ue -c /home/vagrant/shared/ueransim/ue0.yaml -i $((supi0+1200)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+1200)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+1200)) -n 400 -t 25 &
sleep 10

sudo nr-ue -c /home/vagrant/shared/ueransim/ue0.yaml -i $((supi0+1600)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+1200)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+1200)) -n 400 -t 25 &
sleep 10

sudo nr-ue -c /home/vagrant/shared/ueransim/ue0.yaml -i $((supi0+2000)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+1200)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+1200)) -n 400 -t 25 &
sleep 10

sudo nr-ue -c /home/vagrant/shared/ueransim/ue0.yaml -i $((supi0+2400)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+1200)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+1200)) -n 400 -t 25 &
sleep 10

sudo nr-ue -c /home/vagrant/shared/ueransim/ue0.yaml -i $((supi0+2800)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+1200)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+1200)) -n 400 -t 25 &
sleep 10

sudo nr-ue -c /home/vagrant/shared/ueransim/ue0.yaml -i $((supi0+3200)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+1200)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+1200)) -n 400 -t 25 &
sleep 10

sudo nr-ue -c /home/vagrant/shared/ueransim/ue0.yaml -i $((supi0+3600)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+1200)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+1200)) -n 400 -t 25 &
sleep 10

sudo nr-ue -c /home/vagrant/shared/ueransim/ue0.yaml -i $((supi0+4000)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+1200)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+1200)) -n 400 -t 25 &
sleep 10

sudo nr-ue -c /home/vagrant/shared/ueransim/ue0.yaml -i $((supi0+4400)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+1200)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+1200)) -n 400 -t 25 &
sleep 10

sudo nr-ue -c /home/vagrant/shared/ueransim/ue0.yaml -i $((supi0+4800)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+1200)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+1200)) -n 400 -t 25 &
sleep 10

sudo nr-ue -c /home/vagrant/shared/ueransim/ue0.yaml -i $((supi0+5200)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+1200)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+1200)) -n 400 -t 25 &
sleep 10

#----#----#----#----#----#----#----#----#----#----#----#----#----#----#----#----#----#----#----#----#----

sudo nr-ue -c /home/vagrant/shared/ueransim/ue0.yaml -i $supi0 -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $supi1 -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $supi2 -n 400 -t 25 &
sleep 10

sudo nr-ue -c /home/vagrant/shared/ueransim/ue0.yaml -i $((supi0+400)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+400)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+400)) -n 400 -t 25 &
sleep 10

sudo nr-ue -c /home/vagrant/shared/ueransim/ue0.yaml -i $((supi0+800)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+800)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+800)) -n 400 -t 25 &
sleep 10

sudo nr-ue -c /home/vagrant/shared/ueransim/ue0.yaml -i $((supi0+1200)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+1200)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+1200)) -n 400 -t 25 &
sleep 10

sudo nr-ue -c /home/vagrant/shared/ueransim/ue0.yaml -i $((supi0+1600)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+1200)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+1200)) -n 400 -t 25 &
sleep 10

sudo nr-ue -c /home/vagrant/shared/ueransim/ue0.yaml -i $((supi0+2000)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+1200)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+1200)) -n 400 -t 25 &
sleep 10

sudo nr-ue -c /home/vagrant/shared/ueransim/ue0.yaml -i $((supi0+2400)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+1200)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+1200)) -n 400 -t 25 &
sleep 10

sudo nr-ue -c /home/vagrant/shared/ueransim/ue0.yaml -i $((supi0+2800)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+1200)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+1200)) -n 400 -t 25 &
sleep 10

sudo nr-ue -c /home/vagrant/shared/ueransim/ue0.yaml -i $((supi0+3200)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+1200)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+1200)) -n 400 -t 25 &
sleep 10

sudo nr-ue -c /home/vagrant/shared/ueransim/ue0.yaml -i $((supi0+3600)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+1200)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+1200)) -n 400 -t 25 &
sleep 10

sudo nr-ue -c /home/vagrant/shared/ueransim/ue0.yaml -i $((supi0+4000)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+1200)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+1200)) -n 400 -t 25 &
sleep 10

sudo nr-ue -c /home/vagrant/shared/ueransim/ue0.yaml -i $((supi0+4400)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+1200)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+1200)) -n 400 -t 25 &
sleep 10

sudo nr-ue -c /home/vagrant/shared/ueransim/ue0.yaml -i $((supi0+4800)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+1200)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+1200)) -n 400 -t 25 &
sleep 10

sudo nr-ue -c /home/vagrant/shared/ueransim/ue0.yaml -i $((supi0+5200)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+1200)) -n 400 -t 25 &
# sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+1200)) -n 400 -t 25 &
sleep 10
