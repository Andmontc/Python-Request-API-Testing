import requests
import json
from util.configurations import *

se = requests.Session()
se.auth = auth = ('Andmontc', getPassword())
url = 'https://api.github.com/user/repos'
response = se.get(url)

print(response.status_code)

cookie = {'visit-month': 'February'}
res = requests.get('http://rahulshettyacademy.com', cookies=cookie)

print(res.status_code)
