from unittest import mock


# 模拟mock封装
def mock_test(mock_method, request_data, url, method, response_data):
    """

    :param mock_method: 模拟的方法名
    :param request_data: 请求数据
    :param url: 请求地址
    :param method: 请求方式
    :param response_data: 响应数据
    :return:
    """
    mock_method = mock.Mock(return_value=response_data)
    res = mock_method(url, method, request_data)
    return res