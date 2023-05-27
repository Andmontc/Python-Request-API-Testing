import requests
import json

response = requests.get('http://216.10.245.166/Library/GetBook.php', params={'AuthorName' : 'Rahul Shetty2'},)

json_response = response.json()
#print(json_response[0]['book_name'])
assert json_response[0]['book_name'] == 'Devops'
assert response.status_code == 200
#print(response.headers)
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'
for book in json_response:
    if book['isbn'] == 'RGHCC':
        #print(book)
        break
        
assert book['book_name'] == 'Learn Appium Automation with Java'
