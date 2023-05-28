import requests
import json
from util.configurations import *
from util.resources import *
from Payload import *

addUrl = getConfig()['API']['endpoint'] + ApiResources.Addbook
delUrl = getConfig()['API']['endpoint'] + ApiResources.deleteBook
headers= {'Content-Type' : 'application/json'}
json_response = requests.post(addUrl, json=addPayload('fefjkjkg'), headers=headers)
print(json_response.json())
print(json_response.json()['ID'])

book_id = json_response.json()['ID']

response_delete = requests.delete(delUrl, json={
    'ID' : book_id
}, headers=headers)
print(response_delete.status_code)

print(response_delete.json())
