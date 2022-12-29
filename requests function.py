
import requests
from bs4 import BeautifulSoup
headers={
       'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36',
       'email':'knowledgecomputer2018@gmail.com',
       'password':'1234qwer@'
       }
f=open('html.txt','w')

#'id':'input-19'
#'id':'input-16'

login_data={
       
       }
with requests.Session() as s:
       url='https://portal.runflare.com/auth/login'
       r=s.get(url,headers=headers)
       print(r.text)
       #soup=BeautifulSoup(r.content,'html5lib')
       #print(soup.find('input',attrs={'id':'input-16'}))
       
       #print(r.encoding)
       f.write(str(r.content))
       #print(str(r.content))
       
