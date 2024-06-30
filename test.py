'''
Author: sean seanzq0331@163.com
Date: 2024-06-25 12:08:07
LastEditors: sean seanzq0331@163.com
LastEditTime: 2024-06-27 23:25:39
FilePath: /queryScore/test.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import openpyxl
from Students import Students


dict = {'bmh': '246305103054', 'zkzh': '630508428', 'sfzh': '511623200812122519', 'class_num': '13班', 'xm': '蒋云翔', 'yw': 88, 'sx': 100, 'yy': 85, 'wl': 62, 'hx': 46, 'sw': 37, 'ddyfz': 40, 'ls': 35, 'dl': 34, 'tyyjk': 65, 'fjf': 0, 'zf': 592, 'lqyx': '普通高中第一批：邻水二中'}

if('lqyx' in dict):
  print(dict.keys())

