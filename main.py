from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen('')


# from bs4 import BeautifulSoup
# sum=0
#
# soup = BeautifulSoup(open('D:\Coding\GitHub\PycharmProjects\Bear-TOC\testFile.html',encoding = 'utf-8', errors='ignore'),'lxml')
# items=soup.findAll('h2')
#
#
# # for i in items:
# #     result=i.text.split("¥")[1]
# #     result=int(result)
# #     sum+=result
#
# csvFile = open('wjdata.csv', 'w',newline='')
# try:
#     writer = csv.writer(csvFile)
#     writer.writerow(('ID','Amount'))
#     for idx,i in enumerate(items):
#         result = int(i.text.split("¥")[1])
#         writer.writerow((idx+1, result))
#
#
# finally:
#     csvFile.close()