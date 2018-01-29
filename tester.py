import json, os

from urllib.request import Request, urlopen

URL = 'http://localhost:8080/post'

message = {
    'title': 'body',
    'body': 'content'
}
header = {
    'Content-Type': 'application/json; charset=utf-8'
}

req = Request(URL, data=json.dumps(message).encode('utf-8'), headers=header)
response = urlopen(req)
print(response.read())