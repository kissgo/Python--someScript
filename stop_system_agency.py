#!/usr/bin/env python
# coding: utf-8

# In[2]:


import winreg
import ctypes
#import get_proxies

# 如果从来没有开过代理 有可能健不存在 会报错
INTERNET_SETTINGS = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                   r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',
                                   0, winreg.KEY_ALL_ACCESS)
# 设置刷新
INTERNET_OPTION_REFRESH = 37
INTERNET_OPTION_SETTINGS_CHANGED = 39
internet_set_option = ctypes.windll.Wininet.InternetSetOptionW


# In[3]:


def set_key(name, value):
    # 修改键值
    _, reg_type = winreg.QueryValueEx(INTERNET_SETTINGS, name)
    winreg.SetValueEx(INTERNET_SETTINGS, name, 0, reg_type, value)



# In[ ]:


# 启用代理
def start():
    stop()  # 先关闭代理,请求的代理一般来自api,如果前一个代理ip失效或者没加入白名单,会请求失败
    proxy = get_proxies()
    ip_port = proxy['http'].split("//", 1)[1]  # 形式: 12.145.32.68:8888
    set_key('ProxyEnable', 1)  # 启用
    # 本地链接不代理
    set_key('ProxyOverride',
            u'localhost;127.*;10.*;172.16.*;172.17.*;172.18.*;172.19.*;172.20.*;172.21.*;172.22.*;172.23.*;172.24.*;172.25.*;172.26.*;172.27.*;172.28.*;172.29.*;172.30.*;172.31.*;192.168.*;127.0.0.1"""')  
    set_key('ProxyServer', u'{}'.format(ip_port))  # 代理IP及端口，将此代理修改为自己的代理IP
    internet_set_option(0, INTERNET_OPTION_REFRESH, 0, 0)
    internet_set_option(0, INTERNET_OPTION_SETTINGS_CHANGED, 0, 0)
    print(f'当前代理: {ip_port}')



# In[4]:


def stop():
    # 停用代理
    set_key('ProxyEnable', 0)  # 停用
    internet_set_option(0, INTERNET_OPTION_REFRESH, 0, 0)
    internet_set_option(0, INTERNET_OPTION_SETTINGS_CHANGED, 0, 0)
    #print('代理已关闭')


# In[5]:


stop()


# In[ ]:

winreg.QueryValueEx(INTERNET_SETTINGS,'ProxyEnable')[0]


