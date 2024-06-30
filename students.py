'''
Author: sean seanzq0331@163.com
Date: 2024-06-25 12:08:07
LastEditors: sean seanzq0331@163.com
LastEditTime: 2024-06-27 23:15:52
FilePath: /queryScore/Students.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
class Students:
  bmh=''
  zkzh=''
  sfzh=''
  verify=''
  xm=''
  class_num=''
  yw=0
  sx=0
  yy=0
  wl=0
  hx=0
  sw=0
  ddyfz=0
  ls=0
  dl=0
  tyyjk=0
  fjf=0
  zf=0
  lqyx=''

  def __init__(self):
    self.zf=self.yw+self.sx+self.yy+self.wl+self.hx+self.sw+self.ddyfz+self.ls+self.dl+self.tyyjk+self.fjf


  def init(self,classNum,xm,bmh,zkzh,sfzh):
    self.classNum=classNum
    self.xm=xm
    self.bmh=bmh
    self.zkzh=zkzh
    self.sfzh=sfzh

  def __str__(self):
    return f'Students(class_num:{self.class_num},xm:{self.xm},bmh:{self.bmh},zkzh:{self.zkzh},sfzh:{self.sfzh})'
  
  def keys(self):
    return ('bmh','zkzh','sfzh','class_num','xm','yw','sx','yy','wl','hx','sw','ddyfz','ls','dl','tyyjk','fjf','zf','lqyx')
  
  def __getitem__(self,item):
    return getattr(self,item)
  
  def __hash__(self):
    return hash(self.bmh+self.zkzh)
  
  def __eq__(self, other):
    if self.bmh == other.bmh and self.zkzh == other.zkzh:
      return True
    else:
      False