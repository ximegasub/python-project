from flask import Flask
from datetime import datetime
import socket
import tzlocal
import json
from netifaces import interfaces, ifaddresses, AF_INET
from pkg_resources import resource_filename

app = Flask(__name__)
FILE_PATH = resource_filename(__name__, "data/details.json")

def read_data(file_path):
    data = None
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        with open(file_path, 'w+') as f:
            data = {}
            data["details"] = []
    finally:
        return data

def save_data(host_details, file_path):
    data = read_data(file_path)
    if data and isinstance(data, dict):
        data.get("details").append(host_details)
        with open(file_path, 'w') as f:
            json.dump(data, f)
    return data

def get_ips():
    ip_addresses = {}
    for ifaceName in interfaces():
        addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
        ip_addresses.update({ifaceName: addresses})
    return ip_addresses

@app.route('/')
def welcome():
    return "Welcome to the docker final project"

@app.route('/details')
def get_details():
    now = datetime.now()
    now_date = now.strftime("%Y-%m-%d")
    now_time = now.strftime("%H:%M:%S")
    tzone_name = tzlocal.get_localzone_name()
    hostname = socket.gethostname()
    host_ip_address = get_ips()
    host_details = {
        "date": now_date,
        "time": now_time,
        "timezone": tzone_name,
        "hostname": hostname,
        "ip_address": host_ip_address,
    }
    
    _ = save_data(host_details, FILE_PATH)
    return host_details

@app.route('/list-details')
def list_details():
    return read_data(FILE_PATH)

if __name__ == "__main__":
    app.run(debug=True)
