"""
Base_Url:https://webmail30.189.cn/w2/
Author:jing
Modify:2020/12/9
"""

import time
import execjs
import requests
from pprint import pprint


class Login(object):

    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd
        self.sess = requests.session()
        self.login_url = ""

    def get_pwd(self):
        with open('get_pwd.js', encoding='utf-8') as f:
            js_pwd = f.read()
        pwd = execjs.compile(js_pwd, cwd=r'E:\node\node_modules\npm\node_modules').call("getpwd", self.pwd)
        return pwd

    def login_(self):
        pwd = self.get_pwd()
        print(pwd)


if __name__ == '__main__':
    user = ""
    pwd = ""

    login = Login(user, pwd)  # TODO: 输入账号&密码  可能会出现 填写验证码的情况 可参照本项目中的其他含有验证码的网站 如 58同城
    login.login_()
