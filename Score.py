# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Score.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import Cal

class Ui_ScoreWindow(object):

    conScore = sqlite3.connect('game.db')
    curScore = conScore.cursor()


    def combo1(self):
        sl = self.cb1.currentText()
        self.curScore.execute("select players from teams where name = '"+sl+"';")
        result = self.curScore.fetchall()
        for record in result:
            self.lw1.addItem(str(record[0]))


    def combo2(self):
        try:
            for i in range(self.lw1.count()):
                pl = self.lw1.item(i).text()
                mt = self.cb2.currentText()
                self.curScore.execute("select ctg from stats where player = '"+pl+"';")
                ctg = self.curScore.fetchone()[0]
                if ctg == 'batsman':
                    pt = Cal.batscore(pl, mt)
                elif ctg == 'bowler':
                    pt = Cal.bowlscore(pl, mt)
                elif ctg == 'all rounder':
                    pt = Cal.allscore(pl, mt)
                self.lw2.addItem(str(pt))
        except Exception as e:
            print(e)


    def calculate(self):
        sc = 0
        for i in range(self.lw2.count()):
            pt = int(self.lw2.item(i).text())
            sc += pt
        self.l1.setText(str(sc))



    def setupUi(self, ScoreWindow):
        ScoreWindow.setObjectName("ScoreWindow")
        ScoreWindow.resize(472, 334)
        self.horizontalLayoutWidget = QtWidgets.QWidget(ScoreWindow)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(79, 30, 311, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cb1 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.cb1.setObjectName("cb1")
        self.horizontalLayout.addWidget(self.cb1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cb2 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.cb2.setObjectName("cb2")
        self.horizontalLayout.addWidget(self.cb2)
        self.line = QtWidgets.QFrame(ScoreWindow)
        self.line.setGeometry(QtCore.QRect(20, 90, 431, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(ScoreWindow)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 140, 431, 151))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lw1 = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.lw1.setObjectName("lw1")
        self.horizontalLayout_2.addWidget(self.lw1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.lw2 = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.lw2.setObjectName("lw2")
        self.horizontalLayout_2.addWidget(self.lw2)
        self.b1 = QtWidgets.QPushButton(ScoreWindow)
        self.b1.setGeometry(QtCore.QRect(184, 300, 91, 23))
        self.b1.setObjectName("b1")
        self.label = QtWidgets.QLabel(ScoreWindow)
        self.label.setGeometry(QtCore.QRect(100, 110, 47, 20))
        self.label.setObjectName("label")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(ScoreWindow)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(310, 110, 81, 21))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.l1 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.l1.setObjectName("l1")
        self.horizontalLayout_3.addWidget(self.l1)

        self.retranslateUi(ScoreWindow)
        self.cb1.currentIndexChanged['int'].connect(self.lw1.clear)
        self.cb2.currentIndexChanged['int'].connect(self.lw2.clear)
        QtCore.QMetaObject.connectSlotsByName(ScoreWindow)

        self.b1.clicked.connect(self.calculate)
        self.cb1.currentIndexChanged.connect(self.combo1)
        self.cb2.currentIndexChanged.connect(self.combo2)
        self.curScore.execute("select distinct name from teams;")
        result = self.curScore.fetchall()
        for record in result:
            self.cb1.addItem(str(record[0]))

        self.curScore.execute("select distinct name from match;")
        result = self.curScore.fetchall()
        for record in result:
            self.cb2.addItem(str(record[0]))

    def retranslateUi(self, ScoreWindow):
        _translate = QtCore.QCoreApplication.translate
        ScoreWindow.setWindowTitle(_translate("ScoreWindow", "Form"))
        self.b1.setText(_translate("ScoreWindow", "Calculate Score"))
        self.label.setText(_translate("ScoreWindow", "Players:"))
        self.label_2.setText(_translate("ScoreWindow", "Points:"))
        self.l1.setText(_translate("ScoreWindow", "##"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ScoreWindow = QtWidgets.QWidget()
    ui = Ui_ScoreWindow()
    ui.setupUi(ScoreWindow)
    ScoreWindow.show()
    sys.exit(app.exec_())

