from base.readExcelData import OperateExcel
from data import data_config
from base.readJson import OperateJson
class GetData:

    def __init__(self):
        self.excelObj = OperateExcel()
        self.jsonObj = OperateJson()
        self.headerData = {
            # "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjE2Mzg2MjZiZmJkMTQwMDNiYjBlM2VjODE1M2NlZTQ5IiwiZXhwIjoxNTc5MjU0Mjc4LCJuYmYiOjE1NzgzOTAyNzh9.f6v39YRuPus68FQk7V82DX5Ta1QF7Kvil_pmLim0v4E",
            "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjE2Mzg2MjZiZmJkMTQwMDNiYjBlM2VjODE1M2NlZTQ5IiwiZXhwIjoxNTc4MTI5MzY0LCJuYmYiOjE1NzcyNjUzNjR9.1kFXabU1lDK2iKP2ncF1mIv7t0G-KBDTJwLtpybG7mU",
            "Content-Type": "application/json"
        }

    """
    获取json中的数据
    """
    def get_data_for_json(self, model):
        return self.jsonObj.get_data(model)

    def rewrite(self, id, key, value):
        self.jsonObj.rewrite_json_file(id, key, value)
        return self.jsonObj.get_data(id)

    """
    获取excel中的数据
    """
    # 获取用例数
    def getCaseCount(self):
        return self.excelObj.get_line()

    # 获取id
    def getId(self, row):
        return self.excelObj.get_cell_value(row, int(data_config.get_id()))

    # 获取测试模块名称
    def getTestName(self, row):
        col = int(data_config.get_TestName())
        return self.excelObj.get_cell_value(row, col)

    # 获取请求数据
    def getRequestData(self, row):
        col = int(data_config.get_Request_Data())
        data = self.excelObj.get_cell_value(row, col)
        if data == '':
            return None
        else:
            return data

    # # 获取依赖数据(请求头数据)
    # def getHeaderData(self, row):
    #     col = int(data_config.get_headerData())
    #     method = eval(str(self.excelObj.get_cell_value(row, col)))
    #     return method

    # 获取请求地址
    def getURL(self, row):
        col = int(data_config.get_url())
        return self.excelObj.get_cell_value(row, col)

    # 获取是否执行
    def getIsRun(self, row):
        flag = None
        col =int(data_config.get_isRun())
        run_model = self.excelObj.get_cell_value(row, col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    def setHeader(self, token):
        self.headerData['Authorization'] = token


    # 获取是否携带header
    def getHeader(self, row, token):
        col = int(data_config.get_header())
        header = self.excelObj.get_cell_value(row, col)
        if header == 'yes':
            self.setHeader(token)
            return self.headerData
        else:
            return None



    # 获取请求方式
    def getRequstMethod(self, row):
        col = int(data_config.get_Request_way())
        method = self.excelObj.get_cell_value(row, col)
        return method

    # 获取预期结果
    def getExpectResult(self, row):
        col = int(data_config.get_Expect())
        method = self.excelObj.get_cell_value(row, col)
        return method

    # 将测试结果写入实际结果
    def writeResult(self, row, content):
        col = int(data_config.get_Result())+1
        method = self.excelObj.write_excel_file(row, col, content)
        return method

    # 根据case_id找到对应的行号
    def getRowNumberByCaseID(self, id):
        col = int(data_config.get_id())
        rowCount = self.excelObj.get_rows()
        for i in range(1, rowCount):
            id_name = self.excelObj.get_cell_value(i, col)
            if id == id_name:
                return i

    # 根据行号获取行内容
    def getRowDateByRowNumber(self, row):
        content = self.excelObj.get_row_content(row)
        return content

    # 根据case_id获取行内容
    def getRowDateByCaseId(self, case_id):
        content = self.excelObj.get_row_content(self.getRowNumberByCaseID(case_id))
        return content

    # 获取依赖数据
    def getDependData(self, row):
        col = int(data_config.get_Data_depend())
        res = self.excelObj.get_cell_value(row, col)
        return res

    # 获取case依赖内容
    def getCaseDepend(self, row):
        content = self.excelObj.get_cell_value(row, int(data_config.get_Case_depend()))
        if content == '':
            return None
        else:
            return content

    # 获取依赖字段
    def getDependField(self, row):
        content = self.excelObj.get_cell_value(row, int(data_config.get_Field_depend()))
        return content

if __name__ == '__main__':
    data = GetData()
    # print(data.getHeader(1))
    # print(data.getRequestData(2))
    # print(data.getIsRun(2))
    # print(data.get_data_for_json(data.getRequestData(1)))
    # data.writeResult(5,"hhhhhh")
    # print(data.getRowNumberByCaseID("useradd"))
    # print(data.getRowDateByCaseId("useradd"))
    # print(data.getRowDateByRowNumber(2))
    print(data.getHeader(3,'ffgggf'))