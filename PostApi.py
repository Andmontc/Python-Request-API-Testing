import requests
import json
from Payload import *

json_response = requests.post('http://216.10.245.166/Library/Addbook.php', json=addPayload('fefjkjkg'), headers={'Content-Type' : 'application/json'})
print(json_response.json())
print(json_response.json()['ID'])

book_id = json_response.json()['ID']

response_delete = requests.delete('http://216.10.245.166/Library/DeleteBook.php', json={
    'ID' : book_id
}, headers={'Content-Type' : 'application/json'})
print(response_delete.status_code)

print(response_delete.json())
