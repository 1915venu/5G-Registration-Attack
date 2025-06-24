# Modular Core Network Setup

This repository contains various scripts and configuration files to quickly setup a testbed, with modular core networks, viz. `Open5gs`, `Free5gc` and `OpenAirInterface`. This setup was primarily used to perform various experiments, on 5G-UE Registration Procedure.

## Directory Structure

- The root directory follows the following directory structure:

1. `./docker_open5gs/:` This directory contains various configuration files and scripts for setting up `Open5gs` as core network and `UERANSIM` as radio-access network.
   
2. `./free5gc-compose/:` This directory contains various configuration files and scripts for setting up `free5gc` as core network.

3. `./oai-cn5g-fed/:` This directory contains various configuration files and scripts for setting up `oai` as core network.

## Setting up the Environment

1. Clone the repository:

```sh
cd ~/Desktop/
git clone https://github.com/spring-iitd/5G-Registration-Attack.git
```

## Running different CN simulations

### 1. Open5gs + UERANSIM

1. Move into the appropriate directory and run the core network services as containers:

```sh
cd ~/Desktop/5G-Registration-Attack/cn-configs/docker_open5gs
./run_all_srv.sh
```

2. In another terminal, start the gNB containers:

```sh
cd ~/Desktop/5G-Registration-Attack/cn-configs/docker_open5gs
sudo ./setup_multi_gnbs.sh
```

3. In another terminal, start the UE containers:

```sh
cd ~/Desktop/5G-Registration-Attack/cn-configs/docker_open5gs
sudo ./setup_multi_ues.sh
```

### 2. free5gc + UERANSIM

1. Move into the appropriate directory and run the core network services as containers:

```sh
cd ~/Desktop/5G-Registration-Attack/cn-configs/free5gc-compose
./run_all_srv.sh
```

2. In another terminal, start the gNB containers:

```sh
cd ~/Desktop/5G-Registration-Attack/cn-configs/docker_open5gs
sudo ./setup_multi_gnbs.sh
```

3. In another terminal, start the UE containers:

```sh
cd ~/Desktop/5G-Registration-Attack/cn-configs/docker_open5gs
sudo ./setup_multi_ues.sh
```

### 3. OAI + UERANSIM

1. Move into the appropriate directory and run the core network services as containers:

```sh
cd ~/Desktop/5G-Registration-Attack/cn-configs/oai-cn5g-fed/docker-compose
./run_all_srv.sh
```

2. In another terminal, start the gNB containers:

```sh
cd ~/Desktop/5G-Registration-Attack/cn-configs/docker_open5gs
sudo ./setup_multi_gnbs.sh
```

3. In another terminal, start the UE containers:

```sh
cd ~/Desktop/5G-Registration-Attack/cn-configs/docker_open5gs
sudo ./setup_multi_ues.sh
```

- <u>_Note:_</u> To force kill all the **containers**, execute:

```sh
cd ~/Desktop/5G-Registration-Attack/cn-configs/docker_open5gs
./kill_all_srv.sh
```

## Author & Contributors

> Prateek Bhaisora _(2023JCS2564)_ <br>
> IIT Delhi SPRING Group ([spring-iitd](https://github.com/spring-iitd)) <br>
> GitHub Profile Link: [prateekbhaisora](https://github.com/prateekbhaisora)