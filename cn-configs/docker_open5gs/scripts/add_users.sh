#!/bin/bash

docker cp ./open5gs-dbctl  mongo:/bin/

read -p "Enter the number of users you want to add: " NUM_USERS

SUBSCRIBER_KEY=465B5CE8B199B49FAA5F0A2EE238A6BC
OPERATOR_KEY=E8ED289DEBA952E4283B54E88E6183CA

for (( i=1; i<=NUM_USERS; i++ ))
do
    SUPI="00101012345$(printf "%04d" $i)"
    echo "Checking if SUPI $SUPI already exists..."

    if sudo docker exec -i mongo /bin/open5gs-dbctl showall | grep -q "$SUPI"; then
        echo "SUPI $SUPI already exists. Skipping..."
    else
        echo "Adding user $i with SUPI: $SUPI"
        sudo docker exec -i mongo /bin/open5gs-dbctl add $SUPI $SUBSCRIBER_KEY $OPERATOR_KEY
    fi
done