import requests

s=requests.Session()

r=s.get('https://www.daneshjooyar.com/')
print(r.text)
