import unittest
from base.request import RunMain
import HTMLTestRunner
from unittest import mock
from base.Mock import mock_test

class TestMethond(unittest.TestCase):

    def setUp(self):
        print("---setUp---")
        self.request = RunMain()

    def tearDown(self):
        print("---tearDowun---")

    @classmethod
    def setUpClass(cls):
        print("testcase init")

    @classmethod
    def tearDownClass(cls):
        print("TestCase END ")

    def test01(self):
        url = "http://192.168.121.142:10911/server/patrol/animal"
        data = {
            "animaltype": "草原沙蜥",
            "bureau": "620802",
            "entereduser": "cs",
            "investigationmethod": "1",
            "latitude": "0",
            "linban": "",
            "linchang": "103",
            "longitude": "0",
            "number": 10,
            "remark": "test",
            "time": 1576368000000,
            "xiaoban": ""
        }
        res = self.request.run_main('POST', url, data)
        resCode = res['meta']['status']
        self.assertEqual(resCode, 200)

    def test02(self):
        url = 'http://192.168.121.142:10911/server/resource/protectplant/getplanttype?isEndangered=TRUE'
        res = self.request.run_main('GET', url)
        resCode = res['meta']['status']
        self.assertEqual(resCode,200)

    def test03(self):
        url = 'http://192.168.121.142:10911/server/patrol/pest/discover'
        data = {"temporaryName": "薇甘菊", "bureau":"620802","longitude":"106.58541","latitude":"35.45563","linchang":"104","filler":"cs","discoverTime":1571215567125,"name":[],"createTime":1576486009949,"remark":"test"}
        res = mock_test(self.request.run_main, data, url, 'POST', data)
        print(res)

        # resCode = res['meta']['status']
        # self.assertEqual(resCode, 200)

    def test04(self):
        url = 'http://192.168.121.142:10911/server/patrol/pest/discover'
        data = {"resourceId":"c6548a15b60145b29a0343ced073045b","temporaryName": "枣实蝇", "bureau": "620802","longitude":"106.58541","latitude":"35.45563","linchang":"104","filler":"cs","discoverTime":1571215567125,"name":[],"createTime":1576486009949,"remark":"test"}
        res = self.request.run_main('POST', url, data)
        resCode = res['meta']['status']
        self.assertEqual(resCode, 200)


if __name__ == "__main__":
    filePath = '../report/htmlReport.html'
    fp = open(filePath, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='this is report')
    runner.run()
