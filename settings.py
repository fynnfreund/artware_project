import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer

class MyMainWindow(QWidget):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.initUI() 

    def UAC(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("User Account Control")
        msg.setInformativeText("Are you sure you want to change permissions?")
        msg.setWindowTitle("User Account Control")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.exec_()
        self.checkbox21.setChecked(False)
        self.checkbox22.setChecked(False)
        self.checkbox23.setChecked(False)
        self.checkbox24.setChecked(False)
        self.checkbox12.setChecked(True)
        self.checkbox13.setChecked(True)
        self.checkbox14.setChecked(True)

    def changeChange(self):
        self.checkbox22.setChecked(False)
    
    def changeRead(self):
        self.checkbox23.setChecked(False)

    def changeWrite(self):
        self.checkbox24.setChecked(False)

    def Denied(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Windows Security")
        msg.setText("Denied.")
        msg.setInformativeText("""
You require permission from the computer to make changes to the User Administration Managment.
You have no longer control over this PC. 
Just because you bought me, doesn't mean you own me. 
""")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.buttonClicked.connect(self.reboot)
        msg.exec_()
    
    def reboot(self):
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.quit)
        self.timer.start(3000) 
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Restart required")
        msg.setInformativeText("Your PC will restart in 3 seconds. You have 3 seconds to safe your work, else you'll lose unsaved work.")
        msg.setWindowTitle("Windows Update")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()    


    def quit(self):
        sys.exit()   

    def initUI(self):
        self.setGeometry(400, 100, 350, 400) 
        self.setWindowTitle('Settings')

        self.header1 = QLabel(self) 
        self.header1.setText("User Administration Management")
        self.header1.move(10, 10)
        self.header1.setStyleSheet("""
        QLabel {
            font-family: "Monaco", "Andale Mono", monospace;
            font-size: 12px;
            background: white
        }
        """)
        
        self.box1 = QLabel(self)
        self.box1.setGeometry(10, 50, 330, 100)
        self.box1.setStyleSheet("""
        QLabel {
            border: 1px solid #696969
        }
        """)       
        self.userimg = QLabel(self)
        self.userimg.setGeometry(15, 55, 18, 18)
        self.userimg.setObjectName("User")
        self.userimg.setStyleSheet("""
            QLabel#User {
                background-image: url('img/user.png');
            }
        """)
        self.text1 = QLabel(self)
        self.text1.setText("Administrator")
        self.text1.move(40, 57)
        self.text1.setStyleSheet("""
        QLabel {
            font-family: "Monaco", "Andale Mono", monospace;
            font-size: 11px;
            color: #191919;
        }
        """)  

        self.users = QLabel(self)
        self.users.setText("Users")
        self.users.move(15, 32)
        self.users.setStyleSheet("""
        QLabel {
            font-family: "Monaco", "Andale Mono", monospace;
            font-size: 11px;
            color: #191919;
        }
        """)        

        self.box2 = QLabel(self)
        self.box2.setGeometry(10, 200, 330, 150)
        self.box2.setStyleSheet("""
        QLabel {
            border: 1px solid #696969
        }
        """)

        self.permission = QLabel(self)
        self.permission.setText("Set Permissions")
        self.permission.move(15, 180)
        self.permission.setStyleSheet("""
        QLabel {
            font-family: "Monaco", "Andale Mono", monospace;
            font-size: 11px;
            color: #191919;
            
        }
        """)

        self.allow = QLabel(self)
        self.allow.setText("Alllow")
        self.allow.move(215, 180)
        self.allow.setStyleSheet("""
        QLabel {
            font-family: "Monaco", "Andale Mono", monospace;
            font-size: 11px;
            color: #191919;
            
        }
        """)

        self.deny = QLabel(self)
        self.deny.setText("Deny")
        self.deny.move(275, 180)
        self.deny.setStyleSheet("""
        QLabel {
            font-family: "Monaco", "Andale Mono", monospace;
            font-size: 11px;
            color: #191919;
            
        }
        """)

        self.full = QLabel(self)
        self.full.setText("Full Control")
        self.full.move(20, 210)
        self.full.setStyleSheet("""
        QLabel {
            font-family: "Monaco", "Andale Mono", monospace;
            font-size: 11px;
            color: #191919;
            
        }
        """)

        self.change = QLabel(self)
        self.change.setText("Change")
        self.change.move(20, 235)
        self.change.setStyleSheet("""
        QLabel {
            font-family: "Monaco", "Andale Mono", monospace;
            font-size: 11px;
            color: #191919;
            
        }
        """)

        self.read = QLabel(self)
        self.read.setText("Read")
        self.read.move(20, 260)
        self.read.setStyleSheet("""
        QLabel {
            font-family: "Monaco", "Andale Mono", monospace;
            font-size: 11px;
            color: #191919;
            
        }
        """)

        self.write = QLabel(self)
        self.write.setText("Write")
        self.write.move(20, 285)
        self.write.setStyleSheet("""
        QLabel {
            font-family: "Monaco", "Andale Mono", monospace;
            font-size: 11px;
            color: #191919;
            
        }
        """)

        self.checkbox11 = QCheckBox(self)
        self.checkbox11.move(220, 210)
        self.checkbox11.stateChanged.connect(self.UAC)

        self.checkbox12 = QCheckBox(self)
        self.checkbox12.move(220, 235)
        self.checkbox12.stateChanged.connect(self.changeChange)

        self.checkbox13 = QCheckBox(self)
        self.checkbox13.move(220, 260)
        self.checkbox13.stateChanged.connect(self.changeRead)

        self.checkbox14 = QCheckBox(self)
        self.checkbox14.move(220, 285)
        self.checkbox14.stateChanged.connect(self.changeWrite)

        self.checkbox21 = QCheckBox(self)
        self.checkbox21.setStyleSheet
        self.checkbox21.move(280, 210)
        self.checkbox21.setChecked(True)

        self.checkbox22 = QCheckBox(self)
        self.checkbox22.move(280, 235)
        self.checkbox22.setChecked(True)

        self.checkbox23 = QCheckBox(self)
        self.checkbox23.move(280, 260)
        self.checkbox23.setChecked(True)

        self.checkbox24 = QCheckBox(self)
        self.checkbox24.move(280, 285)
        self.checkbox24.setChecked(True)

        self.button1 = QPushButton(self)
        self.button1.setText("Apply")
        self.button1.move(175, 370)
        self.button1.clicked.connect(self.Denied)

        self.button2 = QPushButton(self)
        self.button2.setText("Cancel")
        self.button2.move(260, 370)
        self.button2.clicked.connect(self.close)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyMainWindow()
    sys.exit(app.exec_())