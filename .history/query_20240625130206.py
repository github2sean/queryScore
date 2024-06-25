'''
Author: sean seanzq0331@163.com
Date: 2024-06-25 12:08:07
LastEditors: sean seanzq0331@163.com
LastEditTime: 2024-06-25 12:55:31
FilePath: /queryScore/query.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#!/usr/etc/

import requests
import datetime
import os
import ddddocr
from PIL import Image

ocr = ddddocr.DdddOcr(show_ad=False)

host = 'http://182.151.23.226:18004/gacjcx/'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'Host': '182.151.23.226:18004',
        'Referer': 'http://182.151.23.226:18004/gacjcx/', 
}
queryInterface = 'query.do'
verifyInterface= 'verifyCode.do'
current_dir = os.path.dirname(os.path.abspath(__file__))
sheetPath = ''


def gen_code(img)
   
with open('verifyCode.png', 'rb') as f:
  img_bytes = f.read()
res = ocr.classification(img_bytes)


def save_image(url, filename):
  """
  从给定的 URL 下载图片并保存到本地。

  Args:
      url (str): 图片 URL
      filename (str): 要保存的文件名
  """
  try:
    # 使用 requests 获取图片数据
    response = requests.get(url, stream=True)
    response.raise_for_status()  # 检查请求是否成功

    # 打开文件并保存图片数据
    with open(filename, 'wb') as f:
      for chunk in response.iter_content(chunk_size=8192): 
        if chunk:  # 过滤掉空 chunk
          f.write(chunk)
    print(f"图片已保存到 {filename}")

  except requests.exceptions.RequestException as e:
    print(f"下载图片失败: {e}")

# 示例使用
nowTime = str(int(datetime.datetime.now().timestamp()*1000))
image_url = host+verifyInterface+"?d="+nowTime
name = nowTime+".jpg"
# save_image(image_url,name) 

# 打开图像文件
print('pic:'+current_dir+os.sep+'verifyCode.png')
image = Image.open(current_dir+os.sep+'verifyCode.png')
# 使用OCR引擎进行文本识别
text = pytesseract.image_to_string(image,lang='eng')
print(f'text:{text}')

queryParams = {'bmh':'246305102696','zkzh':'630508921','sfzh':'511623200812256728','verify':'verifyParams'}


#res = requests.post(host+queryInterface,data=queryParams)

studentNames = []

#print('res:'+res)









