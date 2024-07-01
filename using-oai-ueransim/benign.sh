#!/bin/bash

docker-compose -f docker-compose-benign_ueransim-vpp.yaml up -d
# Name or ID of the ueransim container
CONTAINER_NAME="benign_ueransim"

# Command to run inside the container
COMMAND="/ueransim/bin/nr-ue -c /ueransim/etc/custom-ue.yaml -n 1"

# Number of times to run the command
REPEAT=10

# Duration to run each command before stopping it (in seconds)
TIMEOUT=5

# Interval in seconds between each run
INTERVAL=3

# Check if the container is running
if docker ps | grep -q $CONTAINER_NAME; then
    echo "Container $CONTAINER_NAME is running. Executing the command $REPEAT times with a timeout of $TIMEOUT seconds each..."
    for ((i=1; i<=REPEAT; i++)); do
        echo "Run #$i"
        
        # Run the command with a timeout
        docker exec -d $CONTAINER_NAME bash -c "$COMMAND"
        
        # Wait for TIMEOUT seconds
        sleep $TIMEOUT
        
    done
    echo "Completed $REPEAT runs."
else
    echo "Container $CONTAINER_NAME is not running. Please start the container first."
    exit 1
fi


