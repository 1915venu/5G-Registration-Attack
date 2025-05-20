#!/bin/bash

PROJECT_NAME=reg_attack

function remove_old_logs() {
    rm -rf ./log
}

function run_core_nw_services() {
    mkdir -p ./log
    
    docker compose -f sa-deploy.yaml -p "$PROJECT_NAME" up -d mongo webui metrics grafana 
    docker compose -f sa-deploy.yaml -p "$PROJECT_NAME" up nrf scp ausf udr udm smf upf amf pcf bsf nssf 
}

function main() {
    remove_old_logs
    run_core_nw_services
}

main