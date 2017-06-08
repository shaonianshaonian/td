# coding=utf-8
import requests
import unittest
import json


url1 = "https://www.jsj1314.cn:8443/loginua/newLogin?appIdentifierType=1&appIdentifier=oBUWywbjvH7fhwd4frplce6NXKVk"
r1 = requests.post(url=url1)
cook = r1.cookies # 获取登录后的cookies

class test_UserAccount(unittest.TestCase):
    """接口名：登录接口"""
    def test_loginCase1(self):
        """测试用例：手机号码未注册"""
        self.url = "https://www.jsj1314.cn:8443/loginua/newLogin"
        self.data = {
            'appIdentifierType': '0',
            'appIdentifier': '17628090405',
            'appCredential': '797979'
        }
        self.r = requests.post(url=self.url, data=self.data)
        print(self.r.json())
        print(self.r.status_code)
        self.assertIn('此账号没有注册！', self.r.text)

    def test_loginCase2(self):
        """测试用例：特殊手机号码"""
        self.url = "https://www.jsj1314.cn:8443/loginua/newLogin"
        self.data = {
            'appIdentifierType': '0',
            'appIdentifier': '17628090406123',
            'appCredential': '797979'
        }
        self.r = requests.post(url=self.url, data=self.data)
        print(self.r.json())
        print(self.r.status_code)
        self.assertIn('此账号没有注册！', self.r.text)

    def test_loginCase3(self):
        """测试用例：密码错误"""
        self.url = "https://www.jsj1314.cn:8443/loginua/newLogin"
        self.data = {
            'appIdentifierType': '0',
            'appIdentifier': '17628090406',
            'appCredential': '787878'
        }
        self.r = requests.post(url=self.url, data=self.data)
        print(self.r.json())
        print(self.r.status_code)
        self.assertIn('用户密码错误！', self.r.text)

    def test_loginCase4(self):
        """测试用例：短密码"""
        self.url = "https://www.jsj1314.cn:8443/loginua/newLogin"
        self.data = {
            'appIdentifierType': '0',
            'appIdentifier': '17628090406',
            'appCredential': '7'
        }
        self.r = requests.post(url=self.url, data=self.data)
        print(self.r.json())
        print(self.r.status_code)
        self.assertIn('用户密码错误！', self.r.text)

    def test_loginCase5(self):
        """测试用例：长密码"""
        self.url = "https://www.jsj1314.cn:8443/loginua/newLogin"
        self.data = {
            'appIdentifierType': '0',
            'appIdentifier': '17628090406',
            'appCredential': 'ABCD123456789ABCDEFGHIJKLMN'
        }
        self.r = requests.post(url=self.url, data=self.data)
        print(self.r.json())
        print(self.r.status_code)
        self.assertIn('用户密码错误！', self.r.text)

    def test_loginCase6(self):
        """测试用例：含有特殊符号的密码"""
        self.url = "https://www.jsj1314.cn:8443/loginua/newLogin"
        self.data = {
            'appIdentifierType': 0,
            'appIdentifier': 17628090406,
            'appCredential': "/*-+!@#$%^&*"
        }
        self.r = requests.post(url=self.url, data=self.data)
        print(self.r.json())
        print(self.r.status_code)
        self.assertIn('用户密码错误！', self.r.text)

    def test_login2(self):
        """测试用例：第三方登录(微信)"""
        self.url = "https://www.jsj1314.cn:8443/loginua/newLogin"
        self.data = {
            'appIdentifierType': '1',
            "appIdentifier": "oBUWywbjvH7fhwd4frplce6NXKVk"
        }
        self.r = requests.post(url=self.url, data=self.data)
        print(self.r.json())
        print(self.r.status_code)
        self.assertIn('成都市武侯区福锦断段58号4栋1单元', self.r.text)
        self.assertIn('1200000278', self.r.text)
        self.assertIn('phone', self.r.text)

    def test_login3(self):
        """测试用例：第三方登录(qq)"""
        self.url = "https://www.jsj1314.cn:8443/loginua/newLogin"
        self.data = {
            'appIdentifierType': '2',
            "appIdentifier": "F67264AF19E62EC5B66321A47E7D71D3"
        }
        self.r = requests.post(url=self.url, data=self.data)
        print(self.r.json())
        print(self.r.status_code)

        self.assertIn('成都市武侯区福锦断段58号4栋1单元', self.r.text)
        self.assertIn('1200000278', self.r.text)
        self.assertIn('phone', self.r.text)

    def test_login4(self):
        """测试用例：第三方登录(微博)"""
        self.url = "https://www.jsj1314.cn:8443/loginua/newLogin"
        self.data = {
            'appIdentifierType': '3',
            "appIdentifier": "3892063778"
        }
        self.r = requests.post(url=self.url, data=self.data)
        print(self.r.json())
        print(self.r.status_code)
        self.assertIn('成都市武侯区福锦断段58号4栋1单元', self.r.text)
        self.assertIn('1200000278', self.r.text)
        self.assertIn('phone', self.r.text)

    def test_ChangeUser(self,):
        """测试用例：修改昵称"""
        self.url = "https://www.jsj1314.cn:8443/manageua/changeUser"
        self.data = {
            'nickName': "1234"
        }
        self.r = requests.post(url=self.url, data=self.data,cookies=cook)
        print(self.r.json())
        print(self.r.status_code)
        # self.assertIn("1234", self.r.text)
        self.assertEqual('17628090406',self.r.json()["phone"])
        # self.assertIn('nickName', self.r.text)
if __name__ == 'main':
    unittest.main
