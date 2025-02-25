import os
import re
import time
import urllib
import requests
import ssl
from id_validator import validator
import outputer

ssl._create_default_https_context = ssl._create_stdlib_context

from typing import Any

from datetime import datetime
# U know the rules,

# And so do I~
IDCard = input("\u6839\u636e\u76f8\u5173\u6cd5\u5f8b\u6cd5\u89c4\u5bf9\u672a\u6210\u5e74\u4eba\u9632\u6b62\u6c89\u8ff7\u7684\u8981\u6c42\uff0c\u8bf7\u8f93\u5165\u60a8\u7684\u8eab\u4efd\u8bc1\u53f7\uff1a | According to Related Laws that request to stop minors being "
               "addicted, please input you ID:")
if not validator.is_valid(IDCard):
    if not (datetime.today().weekday == 5 or 6 or 7) and (time.strftime("%H", time.localtime()) == 8):
    print("\u7cfb\u7edf\u68c0\u6d4b\u5230\u60a8\u662f\u672a\u6210\u5e74\u4eba\uff0c\u5c06\u9000\u51fa\u8f6f\u4ef6\u3002")
    exit()
else:
    print("\u901a\u8fc7\u9a8c\u8bc1\uff01")
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/51.0.2704.63 Safari/537.36'}

if_proxy = input("Do you want to set proxy server?[Y/n] ")

if if_proxy == "Y":
    if_localhost = input("Localhost?[Y/n] ")
    if if_localhost == "Y":
        http_port = input("HTTP PROXY PORT: ")
        http_proxy = "localhost:" + http_port
        https_port = input("HTTPS PROXY PORT: ")
        https_proxy = "localhost:" + https_port
    else:
        http_proxy = input("Type http proxy address here. ")
        https_proxy = input("Type https proxy address here. ")
    proxies: dict[str, Any] = {"http": http_proxy, "https": https_proxy}
    if_test = input("Test the proxy server?[Y/n] ")
    try:
        if if_test == "Y":
            ping_http_proxy = "ping"
            ping_https_proxy = "ping"
            ping_result = os.system("ping")
            if "Lost = 0" in ping_result:
                print("Connected to the http proxy server. ")
                ping_result = os.system("ping")
            if "Lost = 0" in ping_result:
                print("Connected to the https proxy server. ")
            else:
                print("No proxy server was set. ")
    except:
        print('\033[1;31;40m')
        print('[Warning]Have you set all the proxy server? ')
        print('\033[0m')


class Monyhar:
    def __init__(self):
        print("Welcome to Monyhar Browser ")

    def surf_internet(self):
        html = requests.get(self)
        print(html.status_code)  # print the http code returned.
        print(html.text)  # print text returned.
        html = html.status_code
        return html

    @staticmethod
    def about():
        print("[Info]Monyhar Browser, made by tucaoba233. ")
        print("[Info]©CopyRight 2021-2021 tucaoba233, All Rights Reserved. ")
        print("[Info]This project follow GPL-3.0 License ")
        print("[Info]For more,please visit https://github.com/tucaoba2333/monyhar-lite-MultiLang-kernel ")

    def detection(self):
        print(self)

    def get_html(self):
        html = urllib.request.urlopen(self).read()
        return html

    def save_html(self, file_content):
        #Attention that some chars are not allowed in Windows like  \
        self = re.sub('[\/:*?"<>|]', '_', self)
        with open(self + ".html", "wb") as f:
            f.write(file_content)
            f.close()


url = input("url:   example: https://www.google.com |")
old_url = url

# if re.search("http://", url) is None:
#    url = "http://" + url
if_https = input("Try to connect with https?[Y/n]")
if if_https == "Y":
    try:
        print(outputer.UseStyle('Loading......', mode='blink'))
        req = urllib.request.Request(url=url, headers=headers)
        res = urllib.request.urlopen(req)
        cache = res.read()
        print(cache)
        html = cache
    except:
        print('\033[1;31;40m')
        print("\033[7;31m[ERROR] Failed to connect to the server with HTTPS/SSL connection.\033[1;31;40m")
        print('\030[WARNING] Your connection to this site is not secure.\033[1;31;40m')
        print('\033[0m')
        print("[Info] Do you want to visit anyway?[Yes/n]")
        if_visit = input()
        if if_visit == "Yes":
            try:
                cache = Monyhar.surf_internet(url)
                print(cache)
                html = cache
            except:
                print("Failed.")
        else:
            print("[Info] User cancelled the connection.")
else:
    print('\033[1;31;40m')  # 下一目标输出背景为黑色，颜色红色高亮显示
    print('\030[7;31m[WARNING] Your connection to this site is not secure.\033[1;31;40m')  # 字体颜色红色反白处理
    print('\030[7;31m[WARNING] Connecting to a site without HTTPS/SSL May cant show normally,if you got trouble in '
          'visiting a site,try https.\033[1;31;40m')
    print('\033[0m')
    cache = Monyhar.surf_internet(url)
    print(cache)
    html = cache

if input("Help-About?[Y/n]") == "Y":
    Monyhar.about()
if input("Do you want to download the page?[Y/n]") == "Y":
    Monyhar.save_html(old_url, Monyhar.get_html(url))