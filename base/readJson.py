import json


class OperateJson:

    def __init__(self, jsonDir='../data/data2.json'):
        self.jsonDir = jsonDir
        self.data = self.read_data()

    # 读取json文件中的所有数据
    def read_data(self):
        with open(self.jsonDir, encoding='utf-8') as fp:
            data = json.load(fp)
            return data

    # 根据id关键字获取数据
    def get_data(self, id):
        return self.data[id]

    # 获取新的json文件
    def get_new_json(self, requestDataName, key, newValue):
        json_data = self.read_data()
        with open(self.jsonDir) as fp:
            for item in json_data:
                if item == requestDataName:
                    json_data[item][key] = newValue
        return json_data

    # 根据关键字，键修改值
    def rewrite_json_file(self, requestDataName, key, newValue):
        new_data = self.get_new_json(requestDataName, key, newValue)
        with open(self.jsonDir, 'w', encoding='utf-8') as f:
            json.dump(new_data, f, indent=2)
        print("重写json文件成功")
        self.data = self.read_data()
        # print(self.read_data()[requestDataName])

if __name__ == '__main__':
    jsonObj = OperateJson()
    jsonObj.rewrite_json_file('useredit', 'id', 'retrtete')
    print(jsonObj.get_data('useredit'))