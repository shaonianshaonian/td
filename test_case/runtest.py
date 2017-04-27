import unittest
from HTMLTestRunner import HTMLTestRunner
import time
test_dir = 'D:\\td\\test_case'

discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = 'D:\\td\\test_report\\'+now+'report.html'
    fp = open(filename, "wb")
    runner = HTMLTestRunner(stream=fp,
                            title="行情接口测试报告",
                            description="测试用例执行情况：")
    runner.run(discover)
    fp.close()
