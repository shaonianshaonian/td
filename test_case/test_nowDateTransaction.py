# coding=utf-8
import requests
import unittest
class transaction(unittest.TestCase):
    def setUp(self):
        print("start test")
        pass

    def tearDown(self):
        print("end test")
        pass

class test_transaction(transaction):          #分时K线数据
    """接口名：当日逐笔成交"""
    def test_ag_transaction(self):
        """测试用例：正常获取Ag当日成交"""
        self.url = "https://www.jsj1314.cn:8081/historicalquotation/nowDateTransaction"
        self.data = {
            "contractCode": 'Ag(T+D)'
        }
        self.r = requests.post(url=self.url, data=self.data)
        print(self.r.text)
        print(self.r.status_code)
        self.assertIn('price', self.r.text)
        self.assertIn('amount', self.r.text)
        self.assertIn('transDate', self.r.text)

    def test_au_transaction(self):
        """测试用例：正常获取Au当日成交"""
        self.url = "https://www.jsj1314.cn:8081/historicalquotation/nowDateTransaction"
        self.data = {
            "contractCode": 'Au(T+D)'
        }
        self.r = requests.post(url=self.url, data=self.data)
        print(self.r.text)
        print(self.r.status_code)
        self.assertIn('price', self.r.text)
        self.assertIn('amount', self.r.text)
        self.assertIn('transDate', self.r.text)

    def test_mAu_transaction(self):
        """测试用例：正常获取mAu当日成交"""
        self.url = "https://www.jsj1314.cn:8081/historicalquotation/nowDateTransaction"
        self.data = {
            "contractCode": 'mAu(T+D)'
        }
        self.r = requests.post(url=self.url, data=self.data)
        print(self.r.text)
        print(self.r.status_code)
        self.assertIn('price', self.r.text)
        self.assertIn('amount', self.r.text)
        self.assertIn('transDate', self.r.text)

if __name__ == 'main':
    unittest.main