#!/bin/bash

docker compose -f ../nr-ue.yaml up -d

docker cp ../ueransim/ueransim-ue.yaml nr_ue:/UERANSIM/config/ueransim-ue.yaml
docker cp ../ueransim/ueransim_image_init.sh nr_ue:/ueransim_image_init.sh

docker exec -it nr_ue bash -c "/ueransim_image_init.sh"