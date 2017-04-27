# coding=utf-8
import requests
import unittest
import json


class Exclusives(unittest.TestCase):
    def setUp(self):
        print("start test")
        pass

    def tearDown(self):
        print("end test")
        pass

class test_Exclusives(Exclusives):
    """接口名：独家专栏"""
    def test_Like(self):
        """测试用例：点赞专栏"""
        self.url = "http://newapi.jsjsy.com/api/exclusives/5/like"
        self.data = {
            "user_id":207
        }
        self.r = requests.post(url=self.url,data=self.data)
        print(self.r.status_code)
        print(self.r.json())
        self.assertIn('200',self.r.text)

    def test_Complaint(self):
        """测试用例：投诉专栏评论"""
        self.url = "http://newapi.jsjsy.com/api/exclusives/comments/5/complaint"
        self.data = {
            "user_id": 207,
            "content": "脏话"
        }
        self.r = requests.post(url=self.url, data=self.data)
        print(self.r.status_code)
        print(self.r.json())
        self.assertIn('投诉成功',self.r.text)
        self.assertIn('200',self.r.text)
if __name__ == 'main':
    unittest.main
