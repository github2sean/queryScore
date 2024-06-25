'''
Author: sean seanzq0331@163.com
Date: 2024-06-25 12:08:07
LastEditors: sean seanzq0331@163.com
LastEditTime: 2024-06-25 14:53:40
FilePath: /queryScore/test.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import datetime
import js
nowTime = str(int(datetime.datetime.now().timestamp()*1000))
print(nowTime)
queryParams = {'bmh':'246305102696','zkzh':'630508921','sfzh':'511623200812256728','verify':verifycode}

print(json.dumps(queryParams))