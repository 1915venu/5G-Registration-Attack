#!/bin/bash

NUM_GNBs=1
GNB_DIR_NAME=multi-gnb
PROJECT_NAME=reg_attack_gnb
GNB_BIN_PATH=/UERANSIM/build
GNB_CFG_PATH=/UERANSIM/config

function remove_old_files() {
    rm -rf ./log-gnbs

    for i in $(seq 1 $NUM_GNBs); do
        cd ./multi-gnb

        rm -rf nr-gnb${i}.yaml
        rm -rf ueransim-gnb${i}_init.sh
        rm -rf ueransim-gnb${i}.yaml

        cd ../
    done
}

function create_gnb_setup_files() {
    local i="$1"
    echo "Creating setup files for gNB-$i..."

    cd ./multi-gnb

    cp nr-gnb-template.yaml nr-gnb${i}.yaml
    cp ueransim-gnb_init-template.sh ueransim-gnb${i}_init.sh
    cp ueransim-gnb-template.yaml ueransim-gnb${i}.yaml

    cd ../
}

function modify_compose_file() {
    local i="$1"

    sed -i "s/^ *container_name: .*/    container_name: nr_gnb${i}/" "nr-gnb${i}.yaml"
    sed -i "s/^ *- COMPONENT_NAME=.*/      - COMPONENT_NAME=ueransim-gnb${i}/" "nr-gnb${i}.yaml"
    # sed -i "s/^ *ipv4_address: .*/        ipv4_address: \${NR_GNB_${i}_IP}/" "nr-gnb${i}.yaml"
    sed -i "s/^ *ipv4_address: .*/        ipv4_address: 172.22.0.$((39 + i))/" "nr-gnb${i}.yaml"
}

function modify_init_script() {
    local i="$i"

    sed -i "s|NR_GNB_IP|NR_GNB_${i}_IP|g" "ueransim-gnb${i}_init.sh"
}

function modify_config_file() {
    local i="$i"

    sed -i "s|NR_GNB_IP|NR_GNB_${i}_IP|g" "ueransim-gnb${i}.yaml"
}

function modify_gnb_setup_files() {
    local i="$1"
    echo "Modifying setup files for gNB-$i..."

    cd ./multi-gnb

    modify_compose_file "$i"
    modify_init_script "$i"
    modify_config_file "$i"

    cd ../
}

function run_multi_gnb() {
    for i in $(seq 1 $NUM_GNBs); do

        create_gnb_setup_files "$i"
        modify_gnb_setup_files "$i"

        CONFIG=./multi-gnb/nr-gnb$i.yaml
        SERVICE_NAME=nr_gnb$i
        PROJECT_NAME=reg_attack_gnb$i

        mkdir -p ./log-gnbs
        touch ./log-gnbs/$SERVICE_NAME.log
        echo "Starting gNB-$i..."
        (
            docker compose -f $CONFIG -p $PROJECT_NAME up -d &&  \
            docker container attach $SERVICE_NAME
        ) > ./log-gnbs/$SERVICE_NAME.log 2>&1 &

        sleep 1s

    done
}

function main() {
    remove_old_files
    run_multi_gnb
}

main