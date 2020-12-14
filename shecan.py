#!/usr/bin/env python3
'''
Get shecan dns servers ips and print them or add them into /etc/resolv.conf file
dependent on your command :) (get | write)
'''
import requests
from bs4 import BeautifulSoup
import sys

colors = {
    'HEADER': '\033[95m',
    'OKBLUE': '\033[94m',
    'OKCYAN': '\033[96m',
    'OKGREEN': '\033[92m',
    'WARNING': '\033[93m',
    'FAIL': '\033[91m',
    'ENDC': '\033[0m',
    'BOLD': '\033[1m',
    'UNDERLINE': '\033[4m'
}

if 'get' or 'write' not in sys.argv:
    sys.argv.append('get')

req = requests.get('https://shecan.ir')
soup = BeautifulSoup(req.text, 'html.parser')
ips = [i.get_text()
       for i in soup.find_all('span', class_='shecan-dns-ips')]

if sys.argv[1] == 'get':
    print(colors['HEADER'] + '=====================================================================')
    [print(colors['OKGREEN'] + colors['BOLD'] + ip + '\n') for ip in ips]
    print(colors['OKCYAN'] + '=====================================================================')

elif sys.argv[1] == 'write':
    try:
        with open('/etc/resolv.conf', 'a') as resolve_file:
            for ip in ips:
                resolve_file.write('\nnameserver ' + ip)
    except PermissionError:
        print(colors['FAIL'] + colors['BOLD'] + 'You should run this command with root privilege')
        sys.exit(1)

else:
    print(colors['WARNING'] + colors['BOLD'] + 'Invalid command recived')
    print(colors['FAIL'] + colors['BOLD'] + 'Valid commands: get | write \n (default => get)')
    sys.exit(1)