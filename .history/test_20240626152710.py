'''
Author: sean seanzq0331@163.com
Date: 2024-06-25 12:08:07
LastEditors: sean seanzq0331@163.com
LastEditTime: 2024-06-26 15:26:57
FilePath: /queryScore/test.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import openpyxl
from Students import Students
sheetTitle = ['班级','姓名','报名号','准考证号','身份证号',语文,数学,英语,物理,化学,生物,道德与法治,历史,地理,体育与健康,加分,总分']

result = openpyxl.Workbook()
sheet_result = result.active
sheet_result.append(sheetTitle)
result.save('中考成绩查询结果.xlsx')


