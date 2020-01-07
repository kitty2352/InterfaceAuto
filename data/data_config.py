class gloabe_var:
    ID = '0'
    TestName = '1'
    URL = '2'
    IsRun = '3'
    Request_way = '4'
    Header = '5'
    Case_depend = '6'
    Data_depend = '7'
    Field_depend = '8'
    Request_Data = '9'
    Expect = '10'
    Result = '11'


# 获取id
def get_id():
    return gloabe_var.ID


# 获取TestName
def get_TestName():
    return gloabe_var.TestName


# 获取请求地址
def get_url():
    return gloabe_var.URL


# 是否运行
def get_isRun():
    return gloabe_var.IsRun


# 获取请求方式
def get_header():
    return gloabe_var.Header


def get_Case_depend():
    return gloabe_var.Case_depend


def get_Data_depend():
    return gloabe_var.Data_depend


def get_Field_depend():
    return gloabe_var.Field_depend


def get_Request_Data():
    return gloabe_var.Request_Data


def get_Request_way():
    return gloabe_var.Request_way


def get_Expect():
    return gloabe_var.Expect


def get_Result():
    return gloabe_var.Result

