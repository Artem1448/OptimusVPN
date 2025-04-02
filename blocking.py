import paramiko
import re

ACTIVE_IP = []
BINDS = {}

host = "194.87.87.21"
p = 22
user = "root"
passw = "zaqxsw123"

activeTcp = "ss -tnp sport = :443"
tacLog = "tail -n 1000 /var/log/xray/access.log | tac"
 
def ssh_receive(command, lines = False):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        global host, p, user, passw
        ssh.connect(hostname=host, port=p, username=user, password=passw)
        stdin, stdout, stderr = ssh.exec_command(command=command)
        output = stdout.read().decode('UTF-8')
        if lines is True:
            lines = output.splitlines()
            return lines
        else: return output
    finally:
        ssh.close()
 

def extract_ip():
    matches = re.findall(r'(?:\[::ffff:)?(\d+\.\d+\.\d+\.\d+)(?:\])?', ssh_receive(activeTcp))
    global ACTIVE_IP
    ACTIVE_IP = set(matches)
    if '194.87.87.21' in ACTIVE_IP:
        ACTIVE_IP.remove('194.87.87.21')
    print(ACTIVE_IP)

def detecting_email():
    extract_ip()
    need_lines = []
    logs = ssh_receive(tacLog, True)
    for ip in ACTIVE_IP:
        for line in logs:
            if ip in line:
                email = line.split('email: ')[-1].strip("'")
                BINDS[ip] = email
                break
    print(BINDS)

detecting_email()
        


