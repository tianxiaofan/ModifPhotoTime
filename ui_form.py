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
    QLineEdit, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSpacerItem, QTabWidget, QTextEdit,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(648, 526)
        self.scrollArea = QScrollArea(Widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(20, 360, 611, 151))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 609, 149))
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
        self.tabWidget = QTabWidget(Widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(20, 40, 611, 311))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 581, 261))
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)

        self.radioButton_CreateTime = QRadioButton(self.groupBox)
        self.radioButton_CreateTime.setObjectName(u"radioButton_CreateTime")
        self.radioButton_CreateTime.setChecked(False)
        self.radioButton_CreateTime.setAutoRepeat(False)
        self.radioButton_CreateTime.setAutoExclusive(True)

        self.gridLayout_2.addWidget(self.radioButton_CreateTime, 6, 0, 1, 3)

        self.lineEdit_PhotoPath = QLineEdit(self.groupBox)
        self.lineEdit_PhotoPath.setObjectName(u"lineEdit_PhotoPath")

        self.gridLayout_2.addWidget(self.lineEdit_PhotoPath, 1, 1, 1, 2)

        self.pushButton_PhotoModif = QPushButton(self.groupBox)
        self.pushButton_PhotoModif.setObjectName(u"pushButton_PhotoModif")

        self.gridLayout_2.addWidget(self.pushButton_PhotoModif, 9, 0, 1, 1)

        self.lineEdit_PhotoCustomTime = QLineEdit(self.groupBox)
        self.lineEdit_PhotoCustomTime.setObjectName(u"lineEdit_PhotoCustomTime")

        self.gridLayout_2.addWidget(self.lineEdit_PhotoCustomTime, 3, 1, 1, 1)

        self.radioButton_NoUse = QRadioButton(self.groupBox)
        self.radioButton_NoUse.setObjectName(u"radioButton_NoUse")
        self.radioButton_NoUse.setChecked(True)
        self.radioButton_NoUse.setAutoRepeat(False)
        self.radioButton_NoUse.setAutoExclusive(True)

        self.gridLayout_2.addWidget(self.radioButton_NoUse, 4, 0, 1, 3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 3, 2, 1, 1)

        self.radioButton_ForceTime = QRadioButton(self.groupBox)
        self.radioButton_ForceTime.setObjectName(u"radioButton_ForceTime")
        self.radioButton_ForceTime.setChecked(False)
        self.radioButton_ForceTime.setAutoRepeat(False)
        self.radioButton_ForceTime.setAutoExclusive(True)

        self.gridLayout_2.addWidget(self.radioButton_ForceTime, 8, 0, 1, 3)

        self.pushButton_SelectPhotoPath = QPushButton(self.groupBox)
        self.pushButton_SelectPhotoPath.setObjectName(u"pushButton_SelectPhotoPath")

        self.gridLayout_2.addWidget(self.pushButton_SelectPhotoPath, 1, 0, 1, 1)

        self.radioButton_CustomTime = QRadioButton(self.groupBox)
        self.radioButton_CustomTime.setObjectName(u"radioButton_CustomTime")
        self.radioButton_CustomTime.setCheckable(True)
        self.radioButton_CustomTime.setChecked(False)
        self.radioButton_CustomTime.setAutoRepeat(False)
        self.radioButton_CustomTime.setAutoExclusive(True)

        self.gridLayout_2.addWidget(self.radioButton_CustomTime, 5, 0, 1, 3)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.groupBox_2 = QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(20, 20, 491, 111))
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lineEdit_FilePath = QLineEdit(self.groupBox_2)
        self.lineEdit_FilePath.setObjectName(u"lineEdit_FilePath")

        self.gridLayout_3.addWidget(self.lineEdit_FilePath, 0, 0, 1, 2)

        self.pushButton_SelectFilePath = QPushButton(self.groupBox_2)
        self.pushButton_SelectFilePath.setObjectName(u"pushButton_SelectFilePath")

        self.gridLayout_3.addWidget(self.pushButton_SelectFilePath, 0, 2, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_FileCustomTime = QLineEdit(self.groupBox_2)
        self.lineEdit_FileCustomTime.setObjectName(u"lineEdit_FileCustomTime")

        self.gridLayout_3.addWidget(self.lineEdit_FileCustomTime, 1, 1, 1, 1)

        self.pushButton_FileModif = QPushButton(self.groupBox_2)
        self.pushButton_FileModif.setObjectName(u"pushButton_FileModif")

        self.gridLayout_3.addWidget(self.pushButton_FileModif, 1, 2, 1, 1)

        self.label_FileMessage = QLabel(self.groupBox_2)
        self.label_FileMessage.setObjectName(u"label_FileMessage")

        self.gridLayout_3.addWidget(self.label_FileMessage, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"\u56fe\u7247\u5c5e\u6027\u65f6\u95f4\u4fee\u6539", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"\u8bf4\u660e\uff1a\u4e3b\u8981\u652f\u6301\u56fe\u7247\u7684\u5c5e\u6027\u4e0a\u7684\u521b\u5efa\u65f6\u95f4\uff0c\u4fee\u6539\u65f6\u95f4\uff0c\u8bbf\u95ee\u65f6\u95f4\u7684\u4fee\u6539\uff0c\u56fe\u7247\u540e\u7f00\u683c\u5f0f\u4e3aJPG\u6216jpg\uff0c\u5176\u5b83\u672a\u652f\u6301", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"\u4fee\u6539\u4e00\u4e2a\u76ee\u5f55\u4e0b\u6240\u6709\u56fe\u7247\u7684\u521b\u5efa\u65f6\u95f4,\u4fee\u6539\u65f6\u95f4,\u8bbf\u95ee\u65f6\u95f4", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"\u81ea\u5b9a\u4e49\u65f6\u95f4\uff1a", None))
        self.radioButton_CreateTime.setText(QCoreApplication.translate("Widget", u"\u4f7f\u7528\u62cd\u6444\u65f6\u95f4\uff0c\u5982\u672a\u83b7\u53d6\u5230\u62cd\u6444\u65f6\u95f4\uff0c\u5219\u4f7f\u7528Exif\u5185\u7684\u521b\u5efa\u65f6\u95f4,\n"
"\u5982\u679c\u521bExif\u5185\u7684\u5efa\u65f6\u95f4\u4e5f\u672a\u83b7\u53d6\u5230\uff0c\u5219\u5c1d\u8bd5\u4f7f\u7528\u6587\u4ef6\u5c5e\u6027\u7684\u521b\u5efa\u65f6\u95f4\uff0c\u5982\u679c\u8fd8\u662f\u83b7\u53d6\u4e0d\u5230\uff0c\u5219\u4e0d\u4fee\u6539", None))
        self.pushButton_PhotoModif.setText(QCoreApplication.translate("Widget", u"\u5f00\u59cb\u4fee\u6539", None))
        self.lineEdit_PhotoCustomTime.setPlaceholderText(QCoreApplication.translate("Widget", u"2016:06:15 19:20:00", None))
        self.radioButton_NoUse.setText(QCoreApplication.translate("Widget", u"\u4f7f\u7528\u62cd\u6444\u65f6\u95f4\uff0c\u5982\u672a\u83b7\u53d6\u5230\u62cd\u6444\u65f6\u95f4\uff0c\u5219\u4e0d\u4fee\u6539", None))
        self.radioButton_ForceTime.setText(QCoreApplication.translate("Widget", u"\u4e0d\u4f7f\u7528\u62cd\u6444\u65f6\u95f4\uff0c\u5f3a\u5236\u4f7f\u7528\u81ea\u5b9a\u4e49\u65f6\u95f4", None))
        self.pushButton_SelectPhotoPath.setText(QCoreApplication.translate("Widget", u"\u9009\u62e9\u56fe\u7247\u6587\u4ef6\u5939", None))
        self.radioButton_CustomTime.setText(QCoreApplication.translate("Widget", u"\u4f7f\u7528\u62cd\u6444\u65f6\u95f4\uff0c\u5982\u672a\u83b7\u53d6\u5230\u62cd\u6444\u65f6\u95f4\uff0c\u5219\u4f7f\u7528\u81ea\u5b9a\u4e49\u65f6\u95f4", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Widget", u"\u4fee\u6539\u76ee\u5f55\u4e0b\u6240\u6709\u6587\u4ef6", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Widget", u"\u5c06\u4efb\u610f\u4e00\u4e2a\u6587\u4ef6\u7684\u521b\u5efa\u65f6\u95f4,\u4fee\u6539\u65f6\u95f4,\u8bbf\u95ee\u65f6\u95f4\u4fee\u6539\u4e3a\u8bbe\u5b9a\u65f6\u95f4", None))
        self.pushButton_SelectFilePath.setText(QCoreApplication.translate("Widget", u"\u9009\u62e9\u6587\u4ef6", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"\u8bbe\u7f6e\u65f6\u95f4:", None))
        self.lineEdit_FileCustomTime.setPlaceholderText(QCoreApplication.translate("Widget", u"2016:06:15 19:20:00", None))
        self.pushButton_FileModif.setText(QCoreApplication.translate("Widget", u"\u5f00\u59cb\u4fee\u6539", None))
        self.label_FileMessage.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Widget", u"\u5355\u6587\u4ef6\u4fee\u6539", None))
    # retranslateUi

