from data.get_data import GetData
from base.request import RunMain


class DependData:
    """
    处理数据依赖
    """
    def __init__(self, caseid):
        self.operaExcel = GetData()
        self.caseid = caseid

    # 通过case_id获取改case_id 的整行数据
    def get_case_line_data(self, caseId):
        rows_data = self.operaExcel.getRowDateByCaseId(caseId)
        return rows_data

    # 通过依赖数据（data:id）获取执行响应值
    def get_data_for_key(self, depend_data, token):
        key = depend_data.split(":")[0]
        value = depend_data.split(":")[1]
        res = self.run_dependent(token)[key][value]
        return res


    # 执行依赖测试，获取结果
    def run_dependent(self,token):
        run = RunMain()
        rownumber = self.operaExcel.getRowNumberByCaseID(self.caseid)
        url = self.operaExcel.getURL(rownumber)
        data = self.operaExcel.get_data_for_json(self.operaExcel.getRequestData(rownumber))
        header = self.operaExcel.getHeader(rownumber, token)
        res = run.send_post(url, data, header)
        return res


if __name__ == '__main__':
    data = DependData("useradd")
    # print(data.get_data_for_key('data:id','eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjE2Mzg2MjZiZmJkMTQwMDNiYjBlM2VjODE1M2NlZTQ5IiwiZXhwIjoxNTc5MjU0Mjc4LCJuYmYiOjE1NzgzOTAyNzh9.f6v39YRuPus68FQk7V82DX5Ta1QF7Kvil_pmLim0v4E'))