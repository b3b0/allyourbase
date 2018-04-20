import os

def wazuh():
    os.system('echo "ALLYOURBASE" >> /var/log/auth.log')
    print("IT HAS BEEN DONE")

wazuh()
