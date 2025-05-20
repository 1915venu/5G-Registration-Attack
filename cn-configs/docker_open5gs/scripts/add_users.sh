#!/bin/bash

# docker cp webui:/open5gs/misc/db/open5gs-dbctl ./
docker cp ./open5gs-dbctl  mongo:/bin/

read -p "Enter the number of users you want to add: " NUM_USERS

SUBSCRIBER_KEY=8baf473f2f8fd09487cccbd7097c6862
OPERATOR_KEY=11111111111111111111111111111111

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

# rm -rf ./open5gs-dbctl
