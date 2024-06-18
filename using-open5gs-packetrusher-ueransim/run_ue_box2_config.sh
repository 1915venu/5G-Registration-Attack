#!/bin/bash

# Function to run nr-ue and nr-cli with a given SUPI
run_nr_ue_and_nr_cli() {
  local SUPI=$1
  echo $SUPI
  # Function to kill both processes
  cleanup() {
    echo "Cleaning up..."
    kill $NR_UE_PID $NR_CLI_PID
    wait $NR_UE_PID 2>/dev/null
    wait $NR_CLI_PID 2>/dev/null
  }

  # Trap EXIT signal to call cleanup function
  trap cleanup EXIT

  # Start nr-ue with ue.yaml configuration and capture its output
  nr-ue -c ~/shared/ueransim/open5gs-ue.yaml -i $SUPI | tee ~/shared/log/nr-ue-$SUPI.log &
  NR_UE_PID=$!
  echo "Started nr-ue with PID $NR_UE_PID"

  # Monitor nr-ue output for "Initial Registration is successful"
  text_check=""
  while [ -z "$text_check" ]; do
    if grep -q "Initial Registration is successful" ~/shared/log/nr-ue-$SUPI.log; then
      text_check="Initial Registration is successful"
    fi
  done

  echo "Registration is completed"

  # Start nr-cli
  nr-cli imsi-$SUPI -e "deregister switch-off" #| tee ~/shared/log/nr-ue-$SUPI-2.log &
  NR_CLI_PID=$!
  echo "Started nr-cli with PID $NR_CLI_PID"

  rm ~/shared/log/nr-ue-$SUPI.log
  # rm ~/shared/log/nr-ue-$SUPI-2.log
  kill $NR_UE_PID $NR_CLI_PID

}


# Access the arguments
arg1=$1
arg2=$2
declare -i int1=$arg1
declare -i int2=$arg2

# Initialize SUPI value
SUPI=999700000000000
SUPI=$((SUPI + $int1))
COUNTER=1
echo "Starting nr-ue and nr-cli with SUPI $SUPI"

# Loop to call the function with SUPI values 1, 2, and 3
while [ $COUNTER -le $int2 ]; do
  echo "Running with SUPI $SUPI"
  run_nr_ue_and_nr_cli "$SUPI" &
  SUPI=$((SUPI + 1))
  COUNTER=$((COUNTER + 1))
  sleep 0.1
done
wait