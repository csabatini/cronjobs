import requests
import os
from os.path import dirname, exists, join, expanduser, realpath 
from pushbullet import Pushbullet
import json


def get_api_key():
    creds_file = join(expanduser('~'), '.credentials', 'pushbullet.json')
    auth_dict = json.loads(open(creds_file).read().strip())
    return auth_dict.get('api_key', None)


def get_and_compare_ips():
    r = requests.get('http://ipinfo.io')
    current_ip = json.loads(r.text)['ip']

    f = open(join(dirname(realpath(__file__)), 'last_ip.txt'), 'a+')
    last_ip = f.readline().strip()
    f.seek(0)
    f.truncate()
    f.seek(0)
    f.write(current_ip + '\n')
    f.close()
    return None if last_ip == current_ip else current_ip

def send_notification(api_key, ip):
    if ip is not None:
        pb = Pushbullet(api_key)
        pb.push_note("Public IP @ Home changed", "New IP: {}".format(ip))

def main():
    key = get_api_key()
    changed_ip = get_and_compare_ips()
    send_notification(key, changed_ip)

if __name__ == '__main__':
    main()
