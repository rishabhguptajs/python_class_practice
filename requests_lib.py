import requests

x = requests.get('http://172.16.16.16:8090/httpclient.html')

print(x.text)
