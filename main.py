
from bs4 import BeautifulSoup
url=open("testFile.html",encoding = 'utf-8', errors='ignore')
bs=BeautifulSoup(url,'lxml')
collectList=bs.find_all(['h1','h2','h3','h4'])
for i in collectList:
    if i.nmae=='h1':
        print(i.get_text())
    elif i.name=='h2':
        print(" "+i.get_text())
    elif i.name=='h3':
        print("  "+i.get_text())
    elif i.name=='h4':
        print("   "+i.get_text())
