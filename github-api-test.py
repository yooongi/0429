import pprint
import requests

r=requests.get('https://api.github.com/users/stargaeunc-dev')

if r.status_code == 200:
    json_data=r.json()
    pprint.pprint(json_data)

