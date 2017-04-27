import requests
import json
class test_UserAccount():
    """接口名：登录接口"""
    s = requests.session()
    s.get("https://www.jsj1314.cn:8443/loginua/newLogin?appIdentifierType=1&appIdentifier=oBUWywbjvH7fhwd4frplce6NXKVk")
    def test_ChangeUser(self,):
        """测试用例：修改昵称"""
        url1 = "https://www.jsj1314.cn:8443/loginua/newLogin?appIdentifierType=1&appIdentifier=oBUWywbjvH7fhwd4frplce6NXKVk"
        r1 = requests.post(url=url1)
        cook = r1.cookies
        self.url = "https://www.jsj1314.cn:8443/manageua/changeUser"
        self.data = {
            'nickName': "123"
        }
        self.r = requests.post(url=self.url, data=self.data,cookies=cook)
        print(self.r.json())
        print(self.r.status_code)
        self.assertIn("123", self.r.text)