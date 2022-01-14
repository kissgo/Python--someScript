#use the requests module in oder to open DS3617 with WOL
#2021.12.6 5:54AM

import requests
from bs4 import BeautifulSoup

loginUrl = "http://"
url = "http://"

mac = ""

loginData = {
    "luci_username": "",
    "luci_password": ""
}

s = requests.session()
res = s.post(url=loginUrl, data=loginData)
res1 = s.get(url=url)
res1.encoding = res1.apparent_encoding
soup=BeautifulSoup(res1.text,features="lxml")
info = soup.find_all('input',type='hidden')

token = info[0]["value"]
submit = info[1]["value"]

def wol():
    wolData={
        'token': token,
        "cbi.submit": submit,
        "cbid.wol.1.binary":" /usr/bin/wol",
        "cbid.wol.1.mac": mac
    }
    res2=s.post(url=url ,data=wolData)
    res2.encoding=res2.apparent_encoding
    return res2

def etherwake():
    wolData = {
        'token': token,
        "cbi.submit": submit,
        "cbid.wol.1.binary": "/usr/bin/etherwake",
        'cbid.wol.1.iface': 'br-lan',
        "cbid.wol.1.mac": mac
    }
    res2 = s.post(url=url, data=wolData)
    res2.encoding = res2.apparent_encoding
    return res2

res2 = etherwake()
# res2 = wol()

soup = BeautifulSoup(res2.text,features="lxml")


print(str(soup.find("p")).split('<br/>')[-2])