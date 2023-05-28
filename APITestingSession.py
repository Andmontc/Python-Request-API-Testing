import requests
import json
from util.configurations import *

se = requests.Session()
se.auth = auth = ('Andmontc', getPassword())
url = 'https://api.github.com/user/repos'
response = se.get(url)

print(response.status_code)
