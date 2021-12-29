# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'personal.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from chat_bot import ChatBotGraph # 添加
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(525, 556)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(525, 556))
        Dialog.setMaximumSize(QtCore.QSize(525, 556))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/QQicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color:rgb(233, 233, 233)")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 531, 51))
        self.frame.setStyleSheet("background-color: rgb(235, 235, 235);\n"
"color:rgb(85, 85, 85)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 10, 191, 41))
        self.label.setStyleSheet("font: 75 10pt \"Adobe Devanagari\";\n"
"color: rgb(53, 53, 53);")
        self.label.setObjectName("label")
        self.editWindow = QtWidgets.QTextEdit(Dialog)
        self.editWindow.setGeometry(QtCore.QRect(0, 390, 531, 171))
        self.editWindow.setAutoFillBackground(True)
        self.editWindow.setStyleSheet("background-color: rgb(242, 242, 242);border:none")
        self.editWindow.setLineWidth(1)
        self.editWindow.setObjectName("editWindow")
        self.displayWindow = QtWidgets.QTextBrowser(Dialog)
        self.displayWindow.setGeometry(QtCore.QRect(0, 50, 531, 341))
        self.displayWindow.setAutoFillBackground(True)
        self.displayWindow.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.displayWindow.setLineWidth(1)
        self.displayWindow.setMidLineWidth(0)
        self.displayWindow.setObjectName("displayWindow")
        self.sendButton = QtWidgets.QPushButton(Dialog)
        self.sendButton.setGeometry(QtCore.QRect(430, 520, 91, 31))
        self.sendButton.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"color: rgb(79, 79, 79);\n"
"border:none")
        self.sendButton.setObjectName("sendButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "聊天"))
        self.label.setText(_translate("Dialog", "厌食症咨询助理"))
        self.sendButton.setText(_translate("Dialog", "发送"))
        self.displayWindow.append("<h4 >"+"您好，我是厌食症知识助理，可以询问我有关于厌食症的一些内容！"+"</h4>")  # 添加
        self.sendButton.clicked.connect(self.pel_send)  # 添加

    # 添加
    def pel_send(self):
        type1 = "<p style=\"background:#66cc33;font:10pt\">"#margin-top:4px; margin-bottom:4px; margin-left:4px; margin-right:4px; -qt-block-indent:0; text-indent:0px;
        # style=\" background:#f76\"><span style=\" font-size:12pt;\"
        sendtext = self.editWindow.toPlainText()
        if sendtext != ' ':
            self.displayWindow.append("")
            self.displayWindow.insertHtml(type1 + sendtext + "</p>")# </span>
            # self.displayWindow.insertHtml("<a href=\"http://www.cyberhome.cn/images/girl/PLMM_F.jpg\">点击我进入</a>")
            handler = ChatBotGraph()
            answer = handler.chat_main(sendtext)
            self.displayWindow.append("<h4 >" + answer+"</h4>")
        self.editWindow.clear()
