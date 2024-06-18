#!/bin/bash

nr-gnb -c /home/vagrant/shared/ueransim/gnb3.yaml &
nr-gnb -c /home/vagrant/shared/ueransim/gnb4.yaml &
nr-gnb -c /home/vagrant/shared/ueransim/gnb5.yaml &

supi0=999700000026000
supi1=999700000028000
supi2=999700000030000

sudo nr-ue -c /home/vagrant/shared/ueransim/ue3.yaml -i $supi0 -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $supi1 -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $supi2 -n 400 -t 10 &
sleep 4

sudo nr-ue -c /home/vagrant/shared/ueransim/ue3.yaml -i $((supi0+400)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+400)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+400)) -n 400 -t 10 &
sleep 4

sudo nr-ue -c /home/vagrant/shared/ueransim/ue3.yaml -i $((supi0+800)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+800)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+800)) -n 400 -t 10 &
sleep 4

sudo nr-ue -c /home/vagrant/shared/ueransim/ue3.yaml -i $((supi0+1200)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+1200)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+1200)) -n 400 -t 10 &
sleep 4

sudo nr-ue -c /home/vagrant/shared/ueransim/ue3.yaml -i $((supi0+1600)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+1200)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+1200)) -n 400 -t 10 &
sleep 4

sudo nr-ue -c /home/vagrant/shared/ueransim/ue3.yaml -i $((supi0+2000)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+1200)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+1200)) -n 400 -t 10 &
sleep 4

sudo nr-ue -c /home/vagrant/shared/ueransim/ue3.yaml -i $((supi0+2400)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+1200)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+1200)) -n 400 -t 10 &
sleep 4

sudo nr-ue -c /home/vagrant/shared/ueransim/ue3.yaml -i $((supi0+2800)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+1200)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+1200)) -n 400 -t 10 &
sleep 4

sudo nr-ue -c /home/vagrant/shared/ueransim/ue3.yaml -i $((supi0+3200)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+1200)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+1200)) -n 400 -t 10 &
sleep 4

sudo nr-ue -c /home/vagrant/shared/ueransim/ue3.yaml -i $((supi0+3600)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+1200)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+1200)) -n 400 -t 10 &
sleep 4

sudo nr-ue -c /home/vagrant/shared/ueransim/ue3.yaml -i $((supi0+4000)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+1200)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+1200)) -n 400 -t 10 &
sleep 4

sudo nr-ue -c /home/vagrant/shared/ueransim/ue3.yaml -i $((supi0+4400)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+1200)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+1200)) -n 400 -t 10 &
sleep 4

sudo nr-ue -c /home/vagrant/shared/ueransim/ue3.yaml -i $((supi0+4800)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+1200)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+1200)) -n 400 -t 10 &
sleep 4

sudo nr-ue -c /home/vagrant/shared/ueransim/ue3.yaml -i $((supi0+5200)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+1200)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+1200)) -n 400 -t 10 &
sleep 4

sudo nr-ue -c /home/vagrant/shared/ueransim/ue3.yaml -i $supi0 -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $supi1 -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $supi2 -n 400 -t 10 &
sleep 4

sudo nr-ue -c /home/vagrant/shared/ueransim/ue3.yaml -i $((supi0+400)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+400)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+400)) -n 400 -t 10 &
sleep 4

sudo nr-ue -c /home/vagrant/shared/ueransim/ue3.yaml -i $((supi0+800)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+800)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+800)) -n 400 -t 10 &
sleep 4

sudo nr-ue -c /home/vagrant/shared/ueransim/ue3.yaml -i $((supi0+1200)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+1200)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+1200)) -n 400 -t 10 &
sleep 4

sudo nr-ue -c /home/vagrant/shared/ueransim/ue3.yaml -i $((supi0+1600)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+1200)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+1200)) -n 400 -t 10 &
sleep 4

sudo nr-ue -c /home/vagrant/shared/ueransim/ue3.yaml -i $((supi0+2000)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+1200)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+1200)) -n 400 -t 10 &
sleep 4

sudo nr-ue -c /home/vagrant/shared/ueransim/ue3.yaml -i $((supi0+2400)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+1200)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+1200)) -n 400 -t 10 &
sleep 4

sudo nr-ue -c /home/vagrant/shared/ueransim/ue3.yaml -i $((supi0+2800)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+1200)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+1200)) -n 400 -t 10 &
sleep 4

sudo nr-ue -c /home/vagrant/shared/ueransim/ue3.yaml -i $((supi0+3200)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+1200)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+1200)) -n 400 -t 10 &
sleep 4

sudo nr-ue -c /home/vagrant/shared/ueransim/ue3.yaml -i $((supi0+3600)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+1200)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+1200)) -n 400 -t 10 &
sleep 4

sudo nr-ue -c /home/vagrant/shared/ueransim/ue3.yaml -i $((supi0+4000)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+1200)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+1200)) -n 400 -t 10 &
sleep 4

sudo nr-ue -c /home/vagrant/shared/ueransim/ue3.yaml -i $((supi0+4400)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+1200)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+1200)) -n 400 -t 10 &
sleep 4

sudo nr-ue -c /home/vagrant/shared/ueransim/ue3.yaml -i $((supi0+4800)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+1200)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+1200)) -n 400 -t 10 &
sleep 4

sudo nr-ue -c /home/vagrant/shared/ueransim/ue3.yaml -i $((supi0+5200)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue1.yaml -i $((supi1+1200)) -n 400 -t 10 &
sudo nr-ue -c /home/vagrant/shared/ueransim/ue2.yaml -i $((supi2+1200)) -n 400 -t 10 &
sleep 4