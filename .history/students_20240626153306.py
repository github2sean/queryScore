class Students:
  bmh=''
  zkzh=''
  sfzh=''
  verify=''
  xm=''
  classNum=''
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

  def init(self,classNum,xm,bmh,zkzh,sfzh):
    self.classNum=classNum
    self.xm=xm
    self.bmh=bmh
    self.zkzh=zkzh
    self.sfzh=sfzh

  def __str__(self):
    return f'Students(classNum:{self.classNum},xm:{self.xm},bmh:{self.bmh},zkzh:{self.zkzh},sfzh:{self.sfzh})'
  
  def keys(self):
    return ('classNum','xm','')