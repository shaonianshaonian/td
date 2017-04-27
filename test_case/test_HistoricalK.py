# coding=utf-8
import requests
import json
import unittest
class HistoricalK(unittest.TestCase):
    def setUp(self):
        print("start test")
        pass

    def tearDown(self):
        print("end test")
        pass

class test_ag_get(HistoricalK):         #封装Ag(t+d)行情K线类，下面的方法是具体测试用例
    '''接口名：Ag(T+D)行情K线'''

    def test_ag_case1(self):
        '''提交空值常量'''
        self.url = "https://www.jsj1314.cn:8081/historicalquotation/queryHistoricalK"
        self.data = {
            "contractCode": "Ag(T+D)",
            'kType': None
        }
        self.r = requests.post(url=self.url, data=self.data)
        print(self.r.text)
        print(self.r.status_code)
        self.assertIn('412', self.r.text)

    def test_ag_case2(self):
        '''提交常量为负数'''
        self.url = "https://www.jsj1314.cn:8081/historicalquotation/queryHistoricalK"
        self.data = {
            "contractCode": "Ag(T+D)",
            'kType': -1
        }
        self.r = requests.post(url=self.url, data=self.data)
        print(self.r.text)
        print(self.r.status_code)
        self.assertIn('412', self.r.text)

    def test_ag_case3(self):
        '''提交错误合约代码'''
        self.url = "https://www.jsj1314.cn:8081/historicalquotation/queryHistoricalK"
        self.data = {
            "contractCode": "Ag&(T+D)",
            'kType': 1
        }
        self.r = requests.post(url=self.url, data=self.data)
        print(self.r.text)
        print(self.r.status_code)
        self.assertIn('412', self.r.text)

    def test_ag1_get(self):
        '''测试用例：正确获取1分钟'''
        self.url = "https://www.jsj1314.cn:8081/historicalquotation/queryHistoricalK"
        self.data = {
            "contractCode": "Ag(T+D)",
            'kType': '1'
        }
        self.r = requests.post(url=self.url, data=self.data)
        print(self.r.text)
        print(self.r.status_code)
        self.assertIn('upDownRate', self.r.text)

    def test_ag5_get(self):
        '''测试用例：正确获取5分钟'''
        self.url = "https://www.jsj1314.cn:8081/historicalquotation/queryHistoricalK"
        self.data = {
            "contractCode": "Ag(T+D)",
            'kType': '5'
        }
        self.r = requests.post(url=self.url, data=self.data)
        print(self.r.text)
        print(self.r.status_code)
        self.assertIn('upDownRate', self.r.text)

    def test_ag15_get(self):
        '''测试用例：正确获取15分钟'''
        self.url = "https://www.jsj1314.cn:8081/historicalquotation/queryHistoricalK"
        self.data = {
            "contractCode": "Ag(T+D)",
            'kType': '15'
        }
        self.r = requests.post(url=self.url, data=self.data)
        print(self.r.text)
        print(self.r.status_code)
        self.assertIn('upDownRate', self.r.text)

    def test_ag30_get(self):
        '''测试用例：正确获取30分钟'''
        self.url = "https://www.jsj1314.cn:8081/historicalquotation/queryHistoricalK"
        self.data = {
            "contractCode": "Ag(T+D)",
            'kType': '30'
        }
        self.r = requests.post(url=self.url, data=self.data)
        print(self.r.text)
        print(self.r.status_code)
        self.assertIn('upDownRate', self.r.text)
if __name__ == 'main':
    unittest.main