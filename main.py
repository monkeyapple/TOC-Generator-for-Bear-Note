import sys
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QMainWindow,QMessageBox,QApplication,QFileDialog
from uilayout import *

class BearTOC(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.initializing()
        self.ui.htmlDir.clicked.connect(self.select_html)
        self.ui.runButton.clicked.connect(self.scraping)
        self.ui.copyAll.clicked.connect(self.selectAndCopy)

# ----------------Functions------------------------
    def initializing(self):
        self.htmlFilePath=None
        self.scrapResult=""

    def select_html(self):
        self.htmlFilePath=QFileDialog.getOpenFileName(self,'Select HTML File','/home','HTML file(*.html)')
        if self.htmlFilePath[0]:
            self.ui.label_htmlDir.setText(self.htmlFilePath[0])

    def scraping(self):
        if self.htmlFilePath[0]:
            self.htmlData=open(self.htmlFilePath[0])
            url = open("testFile.html", encoding='utf-8', errors='ignore')
            bs = BeautifulSoup(url, 'lxml')
            self.collectList = bs.find_all(['h1', 'h2', 'h3', 'h4'])

        self.scrapResult="# Table of Contents\n"
        for i in self.collectList:
            if i.name=='h1':
                insert=i.get_text()
                self.scrapResult+='*'+' '+'['+insert+']'+'('+self.bearNoteUrl(insert)+')\n'
            elif i.name=='h2':
                insert = i.get_text()
                self.scrapResult+='   '+'['+insert+']'+'('+self.bearNoteUrl(insert)+')\n'
            elif i.name=='h3':
                insert = i.get_text()
                self.scrapResult+='    '+'['+insert+']'+'('+self.bearNoteUrl(insert)+')\n'
            elif i.name=='h4':
                insert = i.get_text()
                self.scrapResult+='     '+'['+insert+']'+'('+self.bearNoteUrl(insert)+')\n'
        self.scrapResult +='***\n'
        self.ui.textBrowser.append(self.scrapResult)

    def bearNoteUrl(self,title):
        if self.ui.identifier.text()!=0:
            id=self.ui.identifier.text()
            self.noteUrl='bear://x-callback-url/open-note?id='+id+'&header='+title
            return(self.noteUrl)
        else:
            QMessageBox.warning(self, 'Warning', 'Please provide the identifier!')

    def selectAndCopy(self):
        if self.ui.textBrowser:
            QApplication.clipboard().setText(self.scrapResult)
            self.finishedPopup()

    def finishedPopup(self):
        msg=QMessageBox()
        msg.setWindowTitle("Info")
        msg.setText("Copied!")
        msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = BearTOC()
    w.show()
    sys.exit(app.exec())

# noteID='332244'
#
# url=open("testFile.html",encoding = 'utf-8', errors='ignore')
# bs=BeautifulSoup(url,'lxml')
# collectList=bs.find_all(['h1','h2','h3','h4'])
#
# def bearNoteUrl(id,title):
#     noteUrl='bear://x-callback-url/open-note?id='+id+'&header='+title
#     return(noteUrl)
#
# def scraping():
#     print('# Table of Contents')
#     for i in collectList:
#         if i.name=='h1':
#             insert=i.get_text()
#             print('*'+' '+'['+insert+']'+'('+bearNoteUrl(noteID,insert)+')')
#         elif i.name=='h2':
#             insert = i.get_text()
#             print('   '+'['+insert+']'+'('+bearNoteUrl(noteID,insert)+')')
#         elif i.name=='h3':
#             insert = i.get_text()
#             print('    '+'['+insert+']'+'('+bearNoteUrl(noteID,insert)+')')
#         elif i.name=='h4':
#             insert = i.get_text()
#             print('     '+'['+insert+']'+'('+bearNoteUrl(noteID,insert)+')')
#     print('***')
# scraping()