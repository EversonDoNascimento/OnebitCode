import os

def shutdown(timer, condition):
    if(condition.upper() == "SIM"):
        os.system(f"sudo shutdown -h +{timer}")
    else:
        os.system("sudo shutdown -c")