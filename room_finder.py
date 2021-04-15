import requests
base_url = 'https://garticphone.com/en/?c='
r = requests.get(f'{base_url}/aaaaaaaaa')
print(r.status_code)