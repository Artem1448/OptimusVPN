import json
import uuid
import subprocess
import os
import signal

path = '/home/Gonna_Destroy/Services/OptimusVPN/x-ray/config.json'

def update_xray():
    result = subprocess.run(['pgrep', 'xray'], capture_output=True, text=True)
    xray_pid = int(result.stdout.strip())
    os.kill(xray_pid, signal.SIGHUP)

def add_client():
    clientID = str(uuid.uuid4())
    newClient = {
        'id': clientID,
        'level': 1
    }
    with open(path, mode='r', encoding='UTF-8') as file:
        data = json.load(file)
        
    data['inbounds'][0]['settings']['clients'].append(newClient)

    with open(path, 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    # update_xray()

def remove_client(uuid = '87a1b413-b0d0-4c19-a3c5-62aa1e29fc84'):

    with open(path, 'r', encoding='UTF-8') as file:
        data = json.load(file)

    clients = data['inbounds'][0]['settings']['clients']

    for client in clients:
        if client['id'] == uuid:
            clients.remove(client)

    data['inbounds'][0]['settings']['clients'] = clients

    with open(path, 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print(clients)

# add_client()
remove_client()