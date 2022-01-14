import time

import requests
import re
import os
from bs4 import BeautifulSoup
from time import sleep

username=""


password = ""

# i录p地址默认为空 取值则为代替别人登

ip=""


headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}
data = {
    "loginType": "",
    "auth_type": "0",
    "isBindMac1": "0",
    "pageid": "4",
    "templatetype": "1",
    "listbindmac": "0",
    "recordmac": "0",
    "isRemind": "0",
    "loginTimes": "",
    "groupId": "",
    "distoken": "",
    "echostr": "",
    "url": "http://1.1.1.1",
    "isautoauth": "",
    "notice_pic_float": " /portal/uploads/pc/hb_pay/images/rrs_bg.jpg",
    "userId": username,
    "passwd": password
}

userId = {
    "userId": username
}

url = "http://1.1.1.1/"
url3 = "http://1.1.1.1:8888/getAuthResult.do"

count=1

def login(ip):
    # 302转跳
    res = requests.get(url=url, allow_redirects=False, headers=headers)
    soup = BeautifulSoup(res.text,features="lxml")
    info = soup.find('script')
    url2 = info.string.split('"')[1].split('"')[0]


    # 是否帮别人登录 替换url的IP地址
    if ip != "":
        print(ip)
        url2 = re.sub(r"(([0-9]{1,3}\.){3}[0-9]{1,3})(?=&)", ip, url2)


    r = requests.post(url=url2, data=data, headers=headers)

    time.sleep(4)#提高检测容错率
    # 判断是否登录成功 英东楼理论上无效
    succ = requests.post(url=url3, data=userId, headers=headers)
    status = succ.text.split('"')[-2]
    if status == "运营商网络拨号成功":
        print(status)
    elif succ.status_code == "200":
        print("英东楼拨号成功")
    else:
        print(str(succ.status_code) + '错误')



while True:
    network = os.system("ping www.baidu.com -w 12 -n 3")#-w 超时 -n 次数  请酌情调整
    if network:
        print('relogin 第{}次'.format(count))
        login(ip)
        count += 1
    else:
        print('正常联网')
    sleep(60*3) # 每多少s检查一次
