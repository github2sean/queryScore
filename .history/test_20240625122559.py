'''
Author: sean seanzq0331@163.com
Date: 2024-06-25 12:08:07
LastEditors: sean seanzq0331@163.com
LastEditTime: 2024-06-25 12:25:15
FilePath: /queryScore/test.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import ddddocr

ocr = ddddocr.DdddOcr(show_ad=Fa)
with open('verifyCode.png', 'rb') as f:
	img_bytes = f.read()
res = ocr.classification(img_bytes)
print('识别出的验证码为：' + res)