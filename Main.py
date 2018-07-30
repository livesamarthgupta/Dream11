# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from Score import Ui_ScoreWindow


class Ui_MainWindow(object):

    conScore = sqlite3.connect('game.db')
    curScore = conScore.cursor()
    bat = bow = all = wk = 0

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ScoreWindow()
        self.ui.setupUi(self.window)
        self.window.show()


    def setWindow(self):
        self.rb1.setCheckable(True)
        self.rb2.setCheckable(True)
        self.rb3.setCheckable(True)
        self.rb4.setCheckable(True)

        self.l1.setText('0')
        self.l2.setText('0')
        self.l3.setText('0')
        self.l4.setText('0')
        self.l5.setText('1000')
        self.l6.setText('0')


    def radio1(self):
        try:
            self.curScore.execute("Select player from stats where ctg = 'batsman';")
            result = self.curScore.fetchall()
            for record in result:
                self.lw1.addItem(str(record[0]))
            for i in range(self.lw2.count()):       # iterate over all List Widget items
                pl = str(self.lw2.item(i).text())
                for j in range(self.lw1.count()):
                    if pl == str(self.lw1.item(j).text()):
                        self.lw1.takeItem(j)
        except Exception as e:
            print(e)


    def radio2(self):
        try:
            self.curScore.execute("Select player from stats where ctg = 'bowler';")
            result = self.curScore.fetchall()
            for record in result:
                self.lw1.addItem(str(record[0]))
            for i in range(self.lw2.count()):       # iterate over all List Widget items
                pl = str(self.lw2.item(i).text())
                for j in range(self.lw1.count()):
                    if pl == str(self.lw1.item(j).text()):
                        self.lw1.takeItem(j)
        except Exception as e:
            print(e)


    def radio3(self):
        try:
            self.curScore.execute("Select player from stats where ctg = 'all rounder';")
            result = self.curScore.fetchall()
            for record in result:
                self.lw1.addItem(str(record[0]))
            for i in range(self.lw2.count()):       # iterate over all List Widget items
                pl = str(self.lw2.item(i).text())
                for j in range(self.lw1.count()):
                    if pl == str(self.lw1.item(j).text()):
                        self.lw1.takeItem(j)
        except Exception as e:
            print(e)


    def radio4(self):
        try:
            self.curScore.execute("Select player from stats where ctg = 'wicket keeper';")
            result = self.curScore.fetchall()
            for record in result:
                self.lw1.addItem(str(record[0]))
            for i in range(self.lw2.count()):       # iterate over all List Widget items
                pl = str(self.lw2.item(i).text())
                for j in range(self.lw1.count()):
                    if pl == str(self.lw1.item(j).text()):
                        self.lw1.takeItem(j)
        except Exception as e:
            print(e)

    def removelist1(self, item):
        try:
            pl = item.text()
            self.curScore.execute("select value from stats where player ='" + pl + "';")
            vl = int(self.curScore.fetchone()[0])
            if int(self.l6.text())+vl < 1000:
                self.curScore.execute("select ctg from stats where player ='" + pl + "';")
                ctg = self.curScore.fetchone()[0]
                if ctg == 'batsman':
                    self.bat = self.bat + 1
                    self.l1.setText(str(self.bat))
                elif ctg == 'bowler':
                    self.bow = self.bow + 1
                    self.l2.setText(str(self.bow))
                elif ctg == 'all rounder':
                    self.all = self.all + 1
                    self.l3.setText(str(self.all))
                elif ctg == 'wicket keeper' and self.wk < 1:
                    self.wk = self.wk + 1
                    self.l4.setText(str(self.wk))
                elif ctg == 'wicket keeper':
                    print("Eror!: Can't Select More Than One Wicket Keeper")
                    return
                self.lw1.takeItem(self.lw1.row(item))
                leftvl = str(int(self.l6.text()) + vl)
                rightvl = str(int(self.l5.text())-vl)
                self.l5.setText(rightvl)
                self.l6.setText(leftvl)
                self.lw2.addItem(item.text())
            else:
                print("Not Enough Points!")
        except Exception as e:
            print(e)


    def removelist2(self, item):
        try:
            pl = item.text()
            self.curScore.execute("select ctg from stats where player ='" + pl + "';")
            ctg = self.curScore.fetchone()[0]
            if ctg == 'batsman':
                self.bat = self.bat + 1
                self.l1.setText(str(self.bat))
            elif ctg == 'bowler':
                self.bow = self.bow + 1
                self.l2.setText(str(self.bow))
            elif ctg == 'all rounder':
                self.all = self.all + 1
                self.l3.setText(str(self.all))
            elif ctg == 'wicket keeper' and self.wk < 1:
                self.wk = self.wk + 1
                self.l4.setText(str(self.wk))
            self.lw2.takeItem(self.lw2.row(item))
            self.curScore.execute("select value from stats where player ='"+pl+"';")
            vl = int(self.curScore.fetchone()[0])
            leftvl = str(int(self.l6.text()) - vl)
            rightvl = str(int(self.l5.text()) + vl)
            self.l5.setText(rightvl)
            self.l6.setText(leftvl)
            self.lw1.addItem(item.text())
        except Exception as e:
            print(e)


    def saveTeam(self):
        try:
            for i in range(self.lw2.count()):       # iterate over all List Widget items
                pl = str(self.lw2.item(i).text())   #Access item from index
                tm = self.l7.text()
                self.curScore.execute("select value from stats where player ='"+pl+"';")
                vl = str(self.curScore.fetchone()[0])
                self.curScore.execute("insert into teams values ('"+tm+"','"+pl+"',"+vl+");")
                self.conScore.commit()
        except Exception as e:
            print(e)
            
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(613, 578)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 220, 591, 271))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lw1 = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.lw1.setObjectName("lw1")
        self.horizontalLayout.addWidget(self.lw1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lw2 = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.lw2.setObjectName("lw2")
        self.horizontalLayout.addWidget(self.lw2)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 100, 571, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.rb1 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.rb1.setObjectName("rb1")
        self.horizontalLayout_2.addWidget(self.rb1)
        self.rb1.setCheckable(False)
        self.rb2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.rb2.setObjectName("rb2")
        self.horizontalLayout_2.addWidget(self.rb2)
        self.rb2.setCheckable(False)
        self.rb3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.rb3.setObjectName("rb3")
        self.horizontalLayout_2.addWidget(self.rb3)
        self.rb3.setCheckable(False)
        self.rb4 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.rb4.setObjectName("rb4")
        self.horizontalLayout_2.addWidget(self.rb4)
        self.rb4.setCheckable(False)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 80, 551, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(30, 10, 551, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 20, 81, 16))
        self.label_5.setObjectName("label_5")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(230, 170, 131, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_3.addWidget(self.label_10)
        self.l7 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.l7.setObjectName("l7")
        self.horizontalLayout_3.addWidget(self.l7)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(60, 170, 141, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.l5 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.l5.setObjectName("l5")
        self.horizontalLayout_4.addWidget(self.l5)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(440, 170, 121, 31))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.l6 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.l6.setObjectName("l6")
        self.horizontalLayout_5.addWidget(self.l6)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(50, 50, 101, 21))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.l1 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.l1.setObjectName("l1")
        self.horizontalLayout_6.addWidget(self.l1)
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(170, 50, 101, 21))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.l2 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.l2.setObjectName("l2")
        self.horizontalLayout_7.addWidget(self.l2)
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(320, 50, 111, 21))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.l3 = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        self.l3.setObjectName("l3")
        self.horizontalLayout_8.addWidget(self.l3)
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(450, 50, 131, 21))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.l4 = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.l4.setObjectName("l4")
        self.horizontalLayout_9.addWidget(self.l4)
        self.horizontalLayoutWidget_10 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(70, 510, 461, 22))
        self.horizontalLayoutWidget_10.setObjectName("horizontalLayoutWidget_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_10)
        self.label.setObjectName("label")
        self.horizontalLayout_10.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_10)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_10.addWidget(self.label_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 613, 21))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNEW_Team = QtWidgets.QAction(MainWindow)
        self.actionNEW_Team.setObjectName("actionNEW_Team")
        self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.menuManage_Teams.addAction(self.actionNEW_Team)
        self.menuManage_Teams.addAction(self.actionOPEN_Team)
        self.menuManage_Teams.addAction(self.actionSAVE_Team)
        self.menuManage_Teams.addAction(self.actionEVALUATE_Team)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        self.retranslateUi(MainWindow)
        self.rb1.toggled['bool'].connect(self.lw1.clear)
        self.rb2.toggled['bool'].connect(self.lw1.clear)
        self.rb3.toggled['bool'].connect(self.lw1.clear)
        self.rb4.toggled['bool'].connect(self.lw1.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.menuManage_Teams.triggered[QtWidgets.QAction].connect(self.menu)
        self.rb1.toggled.connect(self.radio1)
        self.rb2.toggled.connect(self.radio2)
        self.rb3.toggled.connect(self.radio3)
        self.rb4.toggled.connect(self.radio4)
        self.lw1.itemDoubleClicked.connect(self.removelist1)
        self.lw2.itemDoubleClicked.connect(self.removelist2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.rb1.setText(_translate("MainWindow", "Batsman"))
        self.rb2.setText(_translate("MainWindow", "Bowler"))
        self.rb3.setText(_translate("MainWindow", "All Rounder"))
        self.rb4.setText(_translate("MainWindow", "Wicket Keeper"))
        self.label_5.setText(_translate("MainWindow", "Your Selections:"))
        self.label_10.setText(_translate("MainWindow", "Team Name:"))
        self.l7.setText(_translate("MainWindow", "##"))
        self.label_3.setText(_translate("MainWindow", "Points Available: "))
        self.l5.setText(_translate("MainWindow", "##"))
        self.label_4.setText(_translate("MainWindow", "Points Used: "))
        self.l6.setText(_translate("MainWindow", "##"))
        self.label_6.setText(_translate("MainWindow", "Batsmen:"))
        self.l1.setText(_translate("MainWindow", "##"))
        self.label_7.setText(_translate("MainWindow", "Bowlers:"))
        self.l2.setText(_translate("MainWindow", "##"))
        self.label_8.setText(_translate("MainWindow", "All Rounders:"))
        self.l3.setText(_translate("MainWindow", "##"))
        self.label_9.setText(_translate("MainWindow", "Wicket Keepers:"))
        self.l4.setText(_translate("MainWindow", "##"))
        self.label.setText(_translate("MainWindow", "Available Players"))
        self.label_2.setText(_translate("MainWindow", "Selected Players"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNEW_Team.setText(_translate("MainWindow", "NEW Team"))
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))

    def menu(self, action):
        txt = action.text()
        if txt == 'EVALUATE Team':
            self.openWindow()
        elif txt == 'NEW Team':
            self.setWindow()
        elif txt == 'SAVE Team':
            self.saveTeam()  ##Give Definition
        elif txt == 'OPEN Team':
            self.openTeam()  ##Give Definition"""

    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

