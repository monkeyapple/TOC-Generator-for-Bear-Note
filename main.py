import sys
import webbrowser
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QMainWindow,QMessageBox,QApplication,QFileDialog
from uilayout import *

class BearTOC(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.htmlDir.clicked.connect(self.select_html)
        self.ui.runButton.clicked.connect(self.scraping)
        self.ui.copyAll.clicked.connect(self.selectAndCopy)
        self.ui.checkh1.stateChanged.connect(self.asteriskAdd)
        self.ui.checkh2.stateChanged.connect(self.asteriskAdd)
        self.ui.checkh3.stateChanged.connect(self.asteriskAdd)
        self.ui.checkh4.stateChanged.connect(self.asteriskAdd)
        self.ui.checkh5.stateChanged.connect(self.asteriskAdd)
        self.ui.actionMenu.triggered.connect(self.openPage)
        self.htmlFilePath=('','')
        self.scrapResult=''

# ----------------Functions------------------------
    def openPage(self):
        webbrowser.open('https://github.com/monkeyapple/Bear-TOC')

    def select_html(self):
        self.htmlFilePath=QFileDialog.getOpenFileName(self,'Select HTML File','/home','HTML file(*.html)')
        if self.htmlFilePath[0]:
            self.ui.label_htmlDir.setText(self.htmlFilePath[0])

    def asteriskAdd(self):
        self.aster1=''
        self.aster2=''
        self.aster3=''
        self.aster4=''
        self.aster5=''
        if self.ui.checkh1.isChecked() == True:
            self.aster1 = '*'
        if self.ui.checkh2.isChecked() == True:
            self.aster2 = '*'
        if self.ui.checkh3.isChecked() == True:
            self.aster3 = '*'
        if self.ui.checkh4.isChecked() == True:
            self.aster4 = '*'
        if self.ui.checkh5.isChecked() == True:
            self.aster5 = '*'

    def textFormat(self, aster, insert, factor):
        return '\t' * factor+aster+' '+ insert + '(' + self.bearNoteUrl(insert) + ')\n'

    def scraping(self):
        self.ui.textBrowser.clear()
        self.scrapResult = ''
        self.asteriskAdd()
        if self.htmlFilePath[0] != '' and len(self.ui.identifier.text()) != 0:
            url = open(self.htmlFilePath[0], encoding='utf-8', errors='ignore')
            bs = BeautifulSoup(url, 'html.parser')
            self.collectList = bs.find_all(['h1', 'h2', 'h3', 'h4'])
            self.scrapResult = "# Table of Contents\n"
            for i in self.collectList:
                if i.name == 'h1':
                    insert = i.get_text()
                    self.scrapResult+=self.textFormat(self.aster1,insert,0)
                elif i.name == 'h2':
                    insert = i.get_text()
                    self.scrapResult+=self.textFormat(self.aster2,insert,1)
                elif i.name == 'h3':
                    insert = i.get_text()
                    self.scrapResult+=self.textFormat(self.aster3,insert,2)
                elif i.name == 'h4':
                    insert = i.get_text()
                    self.scrapResult+=self.textFormat(self.aster4,insert,3)
                elif i.name == 'h5':
                    insert = i.get_text()
                    self.scrapResult+=self.textFormat(self.aster5,insert,4)
            self.scrapResult += '***\n'
            self.ui.textBrowser.append(self.scrapResult)

        else:
            QMessageBox.warning(self, 'Warning', 'identifier or html file needed!')

    def bearNoteUrl(self,title):
        if len(self.ui.identifier.text())!=0:
            id=self.ui.identifier.text()
            self.noteUrl='bear://x-callback-url/open-note?id='+id+'&header='+title
            return(self.noteUrl)
        else:
            QMessageBox.warning(self, 'Warning', 'Please provide the identifier!')

    def selectAndCopy(self):
        if len(self.scrapResult)!=0:
            QApplication.clipboard().setText(self.scrapResult)
            self.finishedPopup()
        else:
            pass

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