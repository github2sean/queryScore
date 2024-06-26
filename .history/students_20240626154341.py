class Students:
  bmh=''
  zkzh=''
  sfzh=''
  verify=''
  xm=''
  class_num=''
  yw=0
  xx=0
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

  def __init__(self):
    self.zf=self.yw+self.sx+self.yy+self.wl+self.hx+self.sw+self.ddyfz+self.ls+self.d


  def init(self,classNum,xm,bmh,zkzh,sfzh):
    self.classNum=classNum
    self.xm=xm
    self.bmh=bmh
    self.zkzh=zkzh
    self.sfzh=sfzh

  def __str__(self):
    return f'Students(class_num:{self.class_num},xm:{self.xm},bmh:{self.bmh},zkzh:{self.zkzh},sfzh:{self.sfzh})'
  
  def keys(self):
    return ('class_num','xm','bmh','zkzh','sfzh','yw','sx','yy','wl','hx','sw','ddyfz','ls','dl','tyyjk','fjf','zf')
  
  def __getitem__(self,item):
    return getattr(self,item)