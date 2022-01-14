import winreg

import requests
import re
import os
from bs4 import BeautifulSoup
import subprocess
import winreg
import ctypes



username = ""


password = ""

# i录p地址默认为空 取值则为代替别人登
# ip="10.52.177.139"
# ip = "10.52.177.139"
ip = ""

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

# 如果从来没有开过代理 有可能键值不存在 会报错
INTERNET_SETTINGS = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                   r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',
                                   0, winreg.KEY_ALL_ACCESS)
# 设置刷新
INTERNET_OPTION_REFRESH = 37
INTERNET_OPTION_SETTINGS_CHANGED = 39
internet_set_option = ctypes.windll.Wininet.InternetSetOptionW

def set_key(name, value):
    # 修改键值
    _, reg_type = winreg.QueryValueEx(INTERNET_SETTINGS, name)
    winreg.SetValueEx(INTERNET_SETTINGS, name, 0, reg_type, value)

def stop():
    # 停用代理
    set_key('ProxyEnable', 0)  # 停用
    internet_set_option(0, INTERNET_OPTION_REFRESH, 0, 0)
    internet_set_option(0, INTERNET_OPTION_SETTINGS_CHANGED, 0, 0)

#如果开了代理就关闭
if winreg.QueryValueEx(INTERNET_SETTINGS, 'ProxyEnable')[0] == 1:
    stop()

# network = os.system("ping www.baidu.com -w 12 -n 3")  # -w 超时 -n 次数  请酌情调整
network = subprocess.run('ping www.baidu.com -w 12 -n 3', stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)

if network:
    # 302转跳
    res = requests.get(url=url, allow_redirects=False, headers=headers)
    soup = BeautifulSoup(res.text, features="lxml")
    info = soup.find('script')
    url2 = info.string.split('"')[1].split('"')[0]
    r = requests.post(url=url2, data=data, headers=headers)
