import time 
import requests
import os 

os.environ['NO_PROXY'] = '127.0.0.1'
url = 'http://127.0.0.1:8010/getData'
headers = { "content-type": "application/json", "charset": 'utf-8'}

val1 = {"value" : '2'}
val2 = {"value" : '4'}
val3 = {"value" : '6'}
myobj = {"value" : '22'}


while 1:
    x = requests.post(url, headers=headers, json=val1)
    print(x)
    time.sleep(5)
    x = requests.post(url, headers=headers, json=val3)
    print(x)
    time.sleep(5)
    x = requests.post(url, headers=headers, json=myobj)
    print(x)
    time.sleep(5)