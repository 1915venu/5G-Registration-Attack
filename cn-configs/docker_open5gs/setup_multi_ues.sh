#!/bin/bash

NUM_UEs=1
UE_DIR_NAME=multi-ue
UE_BIN_PATH=/UERANSIM/build
UE_CFG_PATH=/UERANSIM/config

function remove_old_files() {
    rm -rf ./log-ues

    for i in $(seq 1 $NUM_UEs); do
        cd ./multi-ue

        rm -rf nr-ue${i}.yaml
        rm -rf ueransim-ue${i}_init.sh
        rm -rf ueransim-ue${i}.yaml

        cd ../
    done
}

function create_ue_setup_files() {
    local i="$1"
    echo "Creating setup files for UE-$i..."

    cd ./multi-ue

    cp nr-ue-template.yaml nr-ue${i}.yaml
    cp ueransim-ue_init-template.sh ueransim-ue${i}_init.sh
    cp ueransim-ue-template.yaml ueransim-ue${i}.yaml

    cd ../
}

function modify_compose_file() {
    local i="$1"

    sed -i "s/^ *container_name: .*/    container_name: nr_ue${i}/" "nr-ue${i}.yaml"
    sed -i "s/^ *- COMPONENT_NAME=.*/      - COMPONENT_NAME=ueransim-ue${i}/" "nr-ue${i}.yaml"
    sed -i "s/^ *ipv4_address: .*/        ipv4_address: 172.22.0.$((62 + i))/" "nr-ue${i}.yaml"
}

function modify_init_script() {
    local i="$i"

    sed -i "s|UE_IMSI|UE_${i}_IMSI|g" "ueransim-ue${i}_init.sh"
    sed -i "s|NR_GNB_IP|NR_GNB_${i}_IP|g" "ueransim-ue${i}_init.sh"
}

function modify_config_file() {
    local i="$i"

    sed -i "s|UE_IMSI|UE_${i}_IMSI|g" "ueransim-ue${i}.yaml"
    sed -i "s|NR_GNB_IP|NR_GNB_${i}_IP|g" "ueransim-ue${i}.yaml"
}

function modify_ue_setup_files() {
    local i="$1"
    echo "Modifying setup files for UE-$i..."

    cd ./multi-ue

    modify_compose_file "$i"
    modify_init_script "$i"
    modify_config_file "$i"

    cd ../
}

function run_multi_ue() {
    for i in $(seq 1 $NUM_UEs); do

        create_ue_setup_files "$i"
        modify_ue_setup_files "$i"

        COMPOSE_FILE="./multi-ue/nr-ue$i.yaml"
        SERVICE_NAME=nr_ue$i
        PROJECT_NAME=reg_attack_ue$i

        mkdir -p ./log-ues
        touch ./log-ues/$SERVICE_NAME.log
        echo "Starting UE-$i..."
        (
            docker compose -f $COMPOSE_FILE -p $PROJECT_NAME up -d && \
            docker container attach $SERVICE_NAME
        ) > ./log-ues/$SERVICE_NAME.log 2>&1 &

    done
}

function main() {
    remove_old_files
    run_multi_ue
}

main