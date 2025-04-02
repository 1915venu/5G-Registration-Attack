# Sending custom NGAP, RRC and NAS Packets

This part of the repository contains code that can be used to send customized `NGAP`, `RRC` and `NAS` messages. It leverages [pycrate](https://github.com/pycrate-org/pycrate) and [pysctp](https://github.com/P1sec/pysctp) libraries of python to achieve this functionality.

## How to setup this Project?

> <u>**Pre-requisites:**</u>

- pip3 and python3.5 _(or, greater)_ installed on your system. For this setup, we will use python 3.10.12.

- A successfully running core network simulator (preferrably [Open5GS](https://github.com/open5gs/open5gs)) and a radio access network simulator (preferrably [UERANSIM](https://github.com/aligungr/UERANSIM)), already set-up on your host machine. For IITD students, please refer [here](https://github.com/spring-iitd/Cellular-Security) for simulator setup.

1. To clone this repository into the `~/shared/` directory, run the following commands:

```sh
cd ~/shared/
git clone https://github.com/spring-iitd/5G-Registration-Attack.git
```

2. Move into the appropriate folder and create a Python Virtual Environment as:

```sh
cd 5G-Registration-Attack/custom-packet-scripts/
sudo apt install python3.10-venv
python3 -m venv py_3.10.12
source py_3.10.12/bin/activate
```

3. Install the required dependencies for this project as:

```sh
pip3 install -r requirements.txt
```

4. Install [CryptoMobile](https://github.com/mitshell/CryptoMobile) toolkit as:

```sh
git clone https://github.com/mitshell/CryptoMobile.git
cd CryptoMobile
sudo apt install python3.10-dev
python3 setup.py install
cd ../
```

## Usage

Once the project is set up, you can use the various scripts provided to perform your simulations. A handy `README.md` file is attached in each sub-directory of this repository, to familiarize you with the setup and usage of various packages.s

## Author & Contributors

> Prateek Bhaisora _(2023JCS2564)_ <br>
> IIT Delhi SPRING Group ([spring-iitd](https://github.com/spring-iitd)) <br>
> GitHub Profile Link: [prateekbhaisora](https://github.com/prateekbhaisora)
