# coding=utf-8
import requests
import unittest
import json

class TimeSharing(unittest.TestCase):
    def setUp(self):
        print("start test")
        pass

    def tearDown(self):
        print("end test")
        pass

class test_timeSharing(TimeSharing):          #分时K线数据
    '''接口名：当日分时数据'''
    def test_timeSharing_case1(self):
        '''提交空值'''
        self.url = "https://www.jsj1314.cn:8081/historicalquotation/nowDateTimeSharing"
        self.data = {
            "contractCode": None
        }
        self.r = requests.post(url=self.url, data=self.data)
        print(self.r.json())
        dicts = json.loads(self.r.text)
        self.assertEqual(dicts['message'], '合约代码参数错误！')
        self.assertIn("code", self.r.text)

    def test_timeShing_case2(self):
        '''提交非String'''
        self.url = "https://www.jsj1314.cn:8081/historicalquotation/nowDateTimeSharing"
        self.data = {
            "contractCode": 123
        }
        self.r = requests.post(url=self.url, data=self.data)
        print(self.r.json())
        dicts = json.loads(self.r.text)
        self.assertEqual(dicts['message'], '合约代码参数错误！')
        self.assertIn("code", self.r.text)

    def test_timeShing_case3(self):
        '''提交含有特殊字符类型的数据'''
        self.url = "https://www.jsj1314.cn:8081/historicalquotation/nowDateTimeSharing"
        self.data = {
            "contractCode": 'Ag(T&D)'
        }
        self.r = requests.post(url=self.url, data=self.data)
        print(self.r.json())
        dicts = json.loads(self.r.text)
        self.assertEqual(dicts['message'], '合约代码参数错误！')
        self.assertIn("code", self.r.text)

    def test_ag_timeSharing(self):
        '''测试用例：正常获取Ag分时数据'''
        self.url = "https://www.jsj1314.cn:8081/historicalquotation/nowDateTimeSharing"
        self.data = {
            "contractCode": 'Ag(T+D)'
        }
        self.r = requests.post(url=self.url, data=self.data)
        print(self.r.text)
        print(self.r.status_code)
        self.assertIn('quoDate', self.r.text)

    def test_au_timeSharing(self):
        '''测试用例：正常获取Au分时数据'''
        self.url = "https://www.jsj1314.cn:8081/historicalquotation/nowDateTimeSharing"
        self.data = {
            "contractCode": 'Au(T+D)'
        }
        self.r = requests.post(url=self.url, data=self.data)
        print(self.r.text)
        print(self.r.status_code)
        self.assertIn('quoDate', self.r.text)

    def test_mAu_timeSharing(self):
        '''测试用例：正常获取mAu分时数据'''
        self.url = "https://www.jsj1314.cn:8081/historicalquotation/nowDateTimeSharing"
        self.data = {
            "contractCode": 'mAu(T+D)'
        }
        self.r = requests.post(url=self.url, data=self.data)
        print(self.r.text)
        print(self.r.status_code)
        self.assertIn('quoDate', self.r.text)
        self.assertIn('open', self.r.text)
        self.assertIn('high', self.r.text)
        self.assertIn('close', self.r.text)
if __name__ == 'main':
    unittest.main()