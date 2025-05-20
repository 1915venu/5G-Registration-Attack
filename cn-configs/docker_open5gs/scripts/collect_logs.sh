#!/bin/bash

OUTPUT_FILENAME="./stats.txt"

if [ -f "$OUTPUT_FILENAME" ]; then 
    echo "Removing old stat file..."
    rm -f "$OUTPUT_FILENAME"
fi

if [ -n "$(docker container ls -aq)" ]; then
    echo "Killing old containers..."
    docker container rm -f $(docker container ls -aq)
fi

echo "Running 5G Core Services..."
docker compose -f ../sa-deploy.yaml -p reg_attack up -d
sleep 5s

echo "Running gNB..."
docker compose -f ../nr-gnb.yaml -p reg_attack up -d
docker cp ../ueransim/ueransim-gnb.yaml nr_gnb:/UERANSIM/config/ueransim-gnb.yaml
docker cp ../ueransim/ueransim_image_init.sh nr_gnb:/ueransim_image_init.sh
docker exec -it nr_gnb bash -c "/ueransim_image_init.sh"
sleep 2s

echo "Running UE..."
docker compose -f ../nr-ue.yaml -p reg_attack up -d
docker cp ../ueransim/ueransim-ue.yaml nr_ue:/UERANSIM/config/ueransim-ue.yaml
docker cp ../ueransim/ueransim_image_init.sh nr_ue:/ueransim_image_init.sh
docker exec -it nr_ue bash -c "/ueransim_image_init.sh"
sleep 2s

# docker container ls

for name in $(docker container ls --format '{{.Names}}'); do
    echo "Collecting logs for $name..." 
    echo "Collecting logs for $name..." >> $OUTPUT_FILENAME 2>&1
    docker stats --no-stream "$name" >> $OUTPUT_FILENAME 2>&1
done