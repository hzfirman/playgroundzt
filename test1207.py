import requests
from bs4 import BeautifulSoup
import re

url="https://bbs.artron.net/thread-4993635-1-1.html"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
response = requests.get(url,headers=headers)
bsobj = BeautifulSoup(response.content, 'html.parser')
linkset=bsobj.find_all("img",{"width":"685"})         #re.compile("https://")
for link in linkset:
    print(link.attrs["file"])