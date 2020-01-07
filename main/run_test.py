from base.commonUtil import CommonUtil
from data.depend_data import DependData
from base.request import RunMain
from data.get_data import GetData
from base.send_email import SendEmail
import json


class RunTest:
    def __init__(self):
        self.run_method = RunMain()
        self.data = GetData()
        self.common = CommonUtil()
        self.emailObj = SendEmail()
        self.token = ''

    def getToken(self):
        url = self.data.getURL(1)
        method = self.data.getRequstMethod(1)
        data = self.data.get_data_for_json('login')
        res = self.run_method.run_main(method, url, data)
        self.token = json.loads(res)['data']['token']

    # 程序执行
    def go_on_run(self):
        row_count = self.data.getCaseCount()
        pass_count = []
        fail_count = []
        self.getToken()

        for i in range(1, row_count):
            test_name = self.data.getTestName(i)
            url = self.data.getURL(i)
            method = self.data.getRequstMethod(i)
            is_run = self.data.getIsRun(i)
            requestDataName = self.data.getRequestData(i)
            data = self.data.get_data_for_json(requestDataName)
            header = self.data.getHeader(i, self.token)
            expect = self.data.getExpectResult(i)
            case_depend = self.data.getCaseDepend(i)
            if is_run:
                if header != None:
                    header = self.data.getHeader(i, self.token)

                if case_depend != None:
                    # 获取依赖数据
                    data_depend = self.data.getDependData(i)
                    # 获取依赖的响应数据
                    depObj = DependData(case_depend)
                    depend_resonse_data = depObj.get_data_for_key(data_depend, self.token)
                    # 获取依赖的key
                    depend_key = self.data.getDependField(i)
                    # 将响应数据赋值给请求数据中的field项中
                    data[depend_key] = depend_resonse_data
                    if method == 'DELETE':
                        url = url + depend_resonse_data

                res = self.run_method.run_main(method, url, data, header)
                m = self.common.is_contain(expect, res)
                # 判断执行结果是否与预期结果一致，并将执行结果写入excel中
                if m:
                    self.data.writeResult(i+1, "pass")
                    pass_count.append(i)
                else:
                    print("接口执行错误-", test_name, ":", res)
                    self.data.writeResult(i+1, res)
                    fail_count.append(i)

        # 将测试结果以邮件方式发出
        # content = "总共执行了" + str(row_count) + "个接口，" + "成功:" + str(len(pass_count)) + ",失败:" + str(len(fail_count))
        # self.emailObj.send_email(["1018404132@qq.com"], "接口测试", content)


if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()