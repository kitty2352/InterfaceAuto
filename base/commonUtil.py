#coding:utf-8
class CommonUtil:
    def is_contain(self, str1, str2):
        """
        判断一个字符串是否在另一个字符串中
        :param str1: 查找的字符串
        :param str2: 被查找的字符串
        :return:
        """
        flag = None
        if isinstance(str1, float):
            str1 = str(str1)

        if str1 in str2:
            flag = True
        else:
            flag = False
        return flag

if __name__ == '__main__':
    com = CommonUtil()
    res = com.is_contain("25366","25366")
    print(res)