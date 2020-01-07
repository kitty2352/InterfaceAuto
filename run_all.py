import unittest
from base import HTMLTestRunner
import os
# 设置执行用例的路径
case_path = os.getcwd() + os.sep + '\\case'
# 设置匹配文件的规则
rule = 'test*.py'
# 查找用例
discover = unittest.defaultTestLoader.discover(start_dir=case_path, pattern=rule)

# 使用相对路径
reportPath = os.getcwd() + os.sep + "report\\report.html"
# reportPath = 'D:\\PyPrg\\web_auto3\\report\\'+'report.html'
fp = open(reportPath, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="测试报告", description="接口自动化测试", )
runner.run(discover)
fp.close()