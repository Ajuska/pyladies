import requests
import json

with open('09/token.txt') as soubor_s_tokenem:
    token = soubor_s_tokenem.read().strip()

headers = {'Authorization': 'token ' + token}

stranka = requests.get('https://api.github.com/emojis',
                        headers=headers)

print(stranka.status_code)
print(stranka.text)
emojis = json.loads(stranka.text)
print(emojis['fire'])

odpoved = requests.put('https://api.github.com/user/starred/pyvec/naucse.python.cz', headers=headers)
print(odpoved)
