# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QTextEdit, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(817, 444)
        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 50, 371, 151))
        self.lineEdit_PhotoPath = QLineEdit(self.groupBox)
        self.lineEdit_PhotoPath.setObjectName(u"lineEdit_PhotoPath")
        self.lineEdit_PhotoPath.setGeometry(QRect(10, 40, 261, 23))
        self.pushButton_SelectPhotoPath = QPushButton(self.groupBox)
        self.pushButton_SelectPhotoPath.setObjectName(u"pushButton_SelectPhotoPath")
        self.pushButton_SelectPhotoPath.setGeometry(QRect(280, 40, 80, 23))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 70, 301, 31))
        self.lineEdit_PhotoCustomTime = QLineEdit(self.groupBox)
        self.lineEdit_PhotoCustomTime.setObjectName(u"lineEdit_PhotoCustomTime")
        self.lineEdit_PhotoCustomTime.setGeometry(QRect(10, 110, 181, 23))
        self.pushButton_PhotoModif = QPushButton(self.groupBox)
        self.pushButton_PhotoModif.setObjectName(u"pushButton_PhotoModif")
        self.pushButton_PhotoModif.setGeometry(QRect(280, 110, 80, 23))
        self.groupBox_2 = QGroupBox(Widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(390, 50, 411, 151))
        self.lineEdit_FilePath = QLineEdit(self.groupBox_2)
        self.lineEdit_FilePath.setObjectName(u"lineEdit_FilePath")
        self.lineEdit_FilePath.setGeometry(QRect(10, 40, 251, 23))
        self.pushButton_SelectFilePath = QPushButton(self.groupBox_2)
        self.pushButton_SelectFilePath.setObjectName(u"pushButton_SelectFilePath")
        self.pushButton_SelectFilePath.setGeometry(QRect(320, 40, 80, 23))
        self.pushButton_FileModif = QPushButton(self.groupBox_2)
        self.pushButton_FileModif.setObjectName(u"pushButton_FileModif")
        self.pushButton_FileModif.setGeometry(QRect(320, 90, 80, 23))
        self.lineEdit_FileCustomTime = QLineEdit(self.groupBox_2)
        self.lineEdit_FileCustomTime.setObjectName(u"lineEdit_FileCustomTime")
        self.lineEdit_FileCustomTime.setGeometry(QRect(80, 90, 151, 23))
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 100, 53, 15))
        self.label_FileMessage = QLabel(self.groupBox_2)
        self.label_FileMessage.setObjectName(u"label_FileMessage")
        self.label_FileMessage.setGeometry(QRect(20, 120, 53, 15))
        self.scrollArea = QScrollArea(Widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 210, 791, 221))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 789, 219))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.textEdit = QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 10, 751, 31))
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"\u56fe\u7247\u5c5e\u6027\u65f6\u95f4\u4fee\u6539", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"\u4fee\u6539\u4e00\u4e2a\u76ee\u5f55\u4e0b\u6240\u6709\u56fe\u7247\u7684\u521b\u5efa\u65f6\u95f4,\u4fee\u6539\u65f6\u95f4,\u8bbf\u95ee\u65f6\u95f4\u4e3a\u62cd\u6444\u65f6\u95f4", None))
        self.pushButton_SelectPhotoPath.setText(QCoreApplication.translate("Widget", u"\u9009\u62e9\u56fe\u7247\u8def\u5f84", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\u8bbe\u7f6e\u4e00\u4e2a\u9ed8\u8ba4\u65f6\u95f4\uff0c\u5982\u679c\u56fe\u7247\u7684\u62cd\u6444\u65f6\u95f4\u6ca1\u6709\u83b7\u53d6\u5230\n"
"\u5219\u4f7f\u7528\u6b64\u65f6\u95f4(\u683c\u5f0f: 2016:06:15 19:20:00)", None))
        self.lineEdit_PhotoCustomTime.setPlaceholderText(QCoreApplication.translate("Widget", u"2016:06:15 19:20:00)", None))
        self.pushButton_PhotoModif.setText(QCoreApplication.translate("Widget", u"\u5f00\u59cb\u4fee\u6539", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Widget", u"\u5c06\u4efb\u610f\u4e00\u4e2a\u6587\u4ef6\u7684\u521b\u5efa\u65f6\u95f4,\u4fee\u6539\u65f6\u95f4,\u8bbf\u95ee\u65f6\u95f4\u4fee\u6539\u4e3a\u8bbe\u5b9a\u65f6\u95f4", None))
        self.pushButton_SelectFilePath.setText(QCoreApplication.translate("Widget", u"\u9009\u62e9\u6587\u4ef6", None))
        self.pushButton_FileModif.setText(QCoreApplication.translate("Widget", u"\u5f00\u59cb\u4fee\u6539", None))
        self.lineEdit_FileCustomTime.setPlaceholderText(QCoreApplication.translate("Widget", u"2016:06:15 19:20:00", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"\u8bbe\u7f6e\u65f6\u95f4:", None))
        self.label_FileMessage.setText("")
        self.label_3.setText(QCoreApplication.translate("Widget", u"\u8bf4\u660e\uff1a\u4e3b\u8981\u652f\u6301\u56fe\u7247\u7684\u5c5e\u6027\u4e0a\u7684\u521b\u5efa\u65f6\u95f4\uff0c\u4fee\u6539\u65f6\u95f4\uff0c\u8bbf\u95ee\u65f6\u95f4\u7684\u4fee\u6539\uff0c\u56fe\u7247\u540e\u7f00\u683c\u5f0f\u4e3aJPG\u6216jpg\uff0c\u5176\u5b83\u672a\u652f\u6301\n"
"\u4f7f\u7528\u524d\u8bf7\u67e5\u770b\u56fe\u7247\u5c5e\u6027\u4e2d\u662f\u5426\u6709\u62cd\u6444\u65f6\u95f4,\u5982\u6ca1\u6709,\u5c06\u4f7f\u7528\u81ea\u5b9a\u4e49\u7684\u65f6\u95f4\u53bb\u4fee\u6539", None))
    # retranslateUi

