#!/bin/bash

# docker cp webui:/open5gs/misc/db/open5gs-dbctl ./
docker cp ./open5gs-dbctl mongo:/bin/

read -p "Enter the number of users you want to delete: " NUM_USERS

for (( i=1; i<=NUM_USERS; i++ ))
do
    SUPI="00101012345$(printf "%04d" $i)"

    echo "Deletion status:"
    sudo docker exec -i mongo /bin/open5gs-dbctl remove $SUPI
    echo " "
done

# rm -rf ./open5gs-dbctl
