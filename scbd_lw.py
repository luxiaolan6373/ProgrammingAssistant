import os
import bs4
path='html/lw/chm/'
files=os.listdir(path)
for f in files:
    fl = os.path.join(path, f)
    if fl.split(".")[-1]=='hhc' or fl.split(".")[-1]=='HHC':
        path=fl
        break
with open(path,'r')as f:
    hhc=f.read()
bs=bs4.BeautifulSoup(hhc,'html.parser')
#print(bs)
UL=bs.find_all('ul')

for item in UL:
    print(item.li.param)



