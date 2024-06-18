import subprocess
import time
import os
import registration as reg
import signal

default_bw = 10
def_sleep = 4

def run_command(command):
    subprocess.run(command, shell=True, text=True)

def attack_core(timeBetweenRegistration, mode='reg'):
    # Start the vagrant environment
    global default_bw
    global def_sleep
    
    sle = int(0.4 * timeBetweenRegistration)
    
    with open(f"./shared/{mode}_rusherbox1.sh", "r") as f:
        lines = f.readlines()
        with open(f"shared/{mode}_rusherbox1.sh", "w") as f:
            for line in lines:
                line = line.replace(f" -t {default_bw}", f" -t {timeBetweenRegistration}")
                line = line.replace(f"sleep {def_sleep}", f"sleep {sle}")    
                f.write(line)

    with open(f"./shared/{mode}_rusherbox2.sh", "r") as f:
        lines = f.readlines()
        with open(f"shared/{mode}_rusherbox2.sh", "w") as f:
            for line in lines:
                line = line.replace(f" -t {default_bw}", f" -t {timeBetweenRegistration}")
                line = line.replace(f"sleep {def_sleep}", f"sleep {sle}")                
                f.write(line)

    default_bw = timeBetweenRegistration
    def_sleep = sle
    
    time.sleep(1)
    
    # Start the open5gs core
    run_command('vagrant ssh open5gs -c "nohup bash /home/vagrant/shared/core_config1.sh > open5gs.log 2>&1 & sleep 1"')
    time.sleep(2)
    
    # Start packet capture with TShark
    tshark_command = f"tshark -i bridge102 -a duration:600 -f 'port 38412' -w {mode}_{timeBetweenRegistration}.pcap &"
    tshark_proc = subprocess.Popen(tshark_command, shell=True)
    print(f"Started TShark with PID: {tshark_proc.pid}")
    
    # Start configurations in vagrant boxes
    box_configs = [
        ('rusher_box1', f'/home/vagrant/shared/{mode}_rusherbox1.sh'),
        ('rusher_box2', f'/home/vagrant/shared/{mode}_rusherbox2.sh'),
        ('ue_box1', '/home/vagrant/shared/ue_box1.sh')
    ]
    for box, config in box_configs:
        run_command(f'vagrant ssh {box} -c "nohup bash {config} 2>%1 & sleep 0.5"')
    

    # Allow operations to proceed for 3 minutes
    time.sleep(600)
    
    box_configs = [
        ('rusher_box1', '/home/vagrant/shared/kill.sh'),
        ('rusher_box2', '/home/vagrant/shared/kill.sh'),
        ('ue_box1', '/home/vagrant/shared/kill.sh'),
        ('open5gs', '/home/vagrant/shared/kill.sh'),
    ]
    for box, config in box_configs:
        run_command(f'vagrant ssh {box} -c "nohup bash {config} 2>%1 & sleep 0.5"')
    
    # run_command('vagrant halt -f &')

    file = f"{mode}_{timeBetweenRegistration}.pcap"
    reg.get_time_taken_to_complete_registration(file)


if __name__ == "__main__":
    list_of_timeBetweenRegistration = [200,150,100,75,50,25,10]
    # for i in list_of_timeBetweenRegistration:
    #     attack_core(timeBetweenRegistration=i, mode='reg')
    # time.sleep(10)
    for i in list_of_timeBetweenRegistration:  
        attack_core(timeBetweenRegistration=i, mode='unreg')
