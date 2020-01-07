#coding:utf-8
import requests
import json

class RunMain:

    def send_post(self, url, data, header):
        res = None
        if header != None:
            res = requests.post(url=url, json=data, headers=header)
        else:
            res = requests.post(url=url, json=data)
        return res.json()

    def send_get(self, url, data, header):
        if header != None:
            res = requests.get(url=url, data=data, headers=header)
        else:
            res = requests.get(url=url, data=data)
        return res.json()

    def send_delete(self, url, data, header):
        if header != None:
            res = requests.delete(url=url, json=data, headers=header)
        else:
            res = requests.delete(url=url, data=data)
        return res.json()

    def send_put(self, url, data, header):
        if header != None:
            res = requests.put(url=url, json=data, headers=header)
        else:
            res = requests.put(url=url, json=data)
        return res.json()


    def run_main(self, method, url, data=None, header=None):
        res = ''
        if method == 'GET':
            res = self.send_get(url, data, header)
        elif method == 'POST':
            res = self.send_post(url, data, header)
        elif method == 'DELETE':
            res = self.send_delete(url, data, header)
        elif method == 'PUT':
            res = self.send_put(url, data, header)
        else:
            print("please input current argument(GET OR POST)")
        return json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)


if __name__ == "__main__":
    addr = "http://192.168.121.31/server/login"
    id = '8002b7c932734660bd2fac6f516225fb'
    addr1 = 'http://192.168.121.31/server/user/delete/'+id
    data = {
        "username": "admin",
        "password": "123"
    }

    headerData = {
        "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjE2Mzg2MjZiZmJkMTQwMDNiYjBlM2VjODE1M2NlZTQ5IiwiZXhwIjoxNTc4MjE2MjY1LCJuYmYiOjE1NzczNTIyNjV9.jUFWhg4mF7TfyrTje1RnecmTjLi_QbVO9s72Zn1N1a8",
        "Content-Type": "application/json"
    }
    putData = {
        "id": "b16be67d6bef4879ab0105e050653a25",
        "nickname": "test",
        "username": "test",
        "password": "123",
        "description": "",
        "organization": "9b2eb34ed49b46da8587859f9ec8a6db",
        "organizationName": "",
        "departmentName": "",
        "roleList": ["4233a1939c9a47b183fcbbf1427ec120"],
        "enable": 0
    }
    putData = json.dumps(putData)
    URL = 'http://192.168.121.31/server/user'
    request = RunMain()
    # print(request.run_main('POST', addr, data))
    print("-----------------------------")
    # print(request.run_main('DELETE', addr1, header=headerData))
    print(type(putData))
    print(request.run_main('PUT', URL, putData, header=headerData))