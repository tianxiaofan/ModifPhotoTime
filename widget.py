# This Python file uses the following encoding: utf-8
import sys
import os
import piexif
from win32file import CreateFile, SetFileTime, GetFileTime, CloseHandle
from win32file import GENERIC_READ, GENERIC_WRITE, OPEN_EXISTING
from pywintypes import Time # 可以忽视这个 Time 报错（运行程序还是没问题的）
import time
import datetime


from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox,QStyleFactory
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget
from PySide6.QtCore import QObject, Signal
from PySide6.QtCore import QCoreApplication
from enum import Enum


time_format = "%Y:%m:%d %H:%M:%S"  # 时间格式

class TimeType(Enum):
    NoneTime = 1
    CustomTime = 2
    CreatTime =  3
    ForceTime = 4

class ModifTime2ShootTime(QObject):
    processMessage = Signal(str)  # 信号声明

    def __init__(self, path):
        super().__init__()
        self.dir_path = path
        self.current_file_path = ""
        self.current_file_time = ""
        self.custom_file_time = "" # 如果没有获取到时间，则使用默认时间
        self.time_type = TimeType.NoneTime

    def modifDirAllFile(self):
        file_name_list = os.listdir(self.dir_path)

        # 从文件夹中获取文件文件
        for file_name in file_name_list:
            if not file_name.lower().endswith(".jpg"):
                continue
            # 生成具体文件路径
            self.current_file_path = self.dir_path + "/" + file_name
            print(self.current_file_path)
            # 提取拍摄时间
            self.readShootTime()
            print(self.current_file_time)

            if self.current_file_time == "":
                self.processMessage.emit(self.current_file_path + " --> 未获取到时间，不修改")  # 发射信号
            else:
                # 写入到 创建时间 修改时间 访问时间
                writeTime(self.current_file_path, self.current_file_time)
                self.processMessage.emit(self.current_file_path + " --> " + self.current_file_time)  # 发射信号

            # 休息一下，防止太快
            time.sleep(0.01)
            QCoreApplication.processEvents()  # 处理事件，确保界面更新
        self.processMessage.emit("end --> ")  # 发射信号


    def readShootTime(self):
        if self.time_type == TimeType.ForceTime:
            self.current_file_time = self.custom_file_time
            return

        create_time =""
        shoot_time = ""

        # 获取拍摄时间
        exif_dict = piexif.load(self.current_file_path)
        try:
            time_str = str(exif_dict["Exif"][36868])
            shoot_time = time_str[2:len(time_str) - 1]
        except:
            shoot_time = ""
        # 获取Exif内文件创建时间
        try:
            create_str = str(exif_dict["Exif"][piexif.ExifIFD.DateTimeOriginal])
            create_time = create_str[2:len(create_str) - 1]
        except:
            create_time = ""

        # 如果没有获取到Exif内创建时间，就获取文件创建时间
        if create_time == "":
            try:
                creation_time = os.path.getctime(self.current_file_path)
                creation_time = datetime.datetime.fromtimestamp(creation_time)
                create_time = creation_time.strftime(time_format)
            except:
                    create_time = ""

        # 如果拍摄时间为空，就用创建时间,如果创建时间也为空，就返回空时间
        if self.time_type == TimeType.CreatTime:
            if shoot_time != "":
                self.current_file_time = shoot_time
            else:
                self.current_file_time = create_time
        elif self.time_type == TimeType.CustomTime:
            if shoot_time != "":
                self.current_file_time = shoot_time
            else:
                self.current_file_time = self.custom_file_time
        elif self.time_type == TimeType.NoneTime:
            self.current_file_time = shoot_time



def timeOffsetAndStruct(times, format, offset):
  return time.localtime(time.mktime(time.strptime(times, format)) + offset)

def writeTime(file_path,file_times):
    # 进行时间偏移 1S，避免创建时间，修改时间，访问时间都一样
    cTime_t = timeOffsetAndStruct(file_times, time_format, 0)
    mTime_t = timeOffsetAndStruct(file_times, time_format, 1)
    aTime_t = timeOffsetAndStruct(file_times, time_format, 2)

    fh = CreateFile(file_path, GENERIC_READ | GENERIC_WRITE, 0, None, OPEN_EXISTING, 0, 0)

    createTimes, accessTimes, modifyTimes = GetFileTime(fh)
    createTimes = Time(time.mktime(cTime_t))
    accessTimes = Time(time.mktime(aTime_t))
    modifyTimes = Time(time.mktime(mTime_t))
    SetFileTime(fh, createTimes, accessTimes, modifyTimes)
    CloseHandle(fh)




class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.pushButton_SelectPhotoPath.clicked.connect(self.selectPhotoPath)
        self.ui.pushButton_SelectFilePath.clicked.connect(self.selectFile)
        self.ui.pushButton_PhotoModif.clicked.connect(self.startModifyPhoto)
        self.ui.pushButton_FileModif.clicked.connect(self.startModifFile)

    # 选择一个文件夹
    def selectPhotoPath(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setOption(QFileDialog.ShowDirsOnly, True)
        dialog.exec()
        # 获取选择的文件夹路径
        path = dialog.selectedFiles()[0]
        # 显示选择的文件夹路径
        self.ui.lineEdit_PhotoPath.setText(path)
        self.ui.textEdit.clear()

    def startModifyPhoto(self):
        # 获取选择的文件夹路径
        path = self.ui.lineEdit_PhotoPath.text()
        if path == "":
            QMessageBox.information(self, "提示", "请选择一个文件夹")
            return

        if self.ui.radioButton_CustomTime.isChecked() or self.ui.radioButton_ForceTime.isChecked():
            # 检查时间格式是否正确 "%Y:%m:%d %H:%M:%S"
                if not self.checkTimeFormat(self.ui.lineEdit_PhotoCustomTime.text(),time_format):
                    QMessageBox.information(self, "提示", "时间格式不正确")
                    return

        modif = ModifTime2ShootTime(path)
        modif.processMessage.connect(self.onProcessMessage)
        modif.custom_file_time = self.ui.lineEdit_PhotoCustomTime.text()
        if self.ui.radioButton_NoUse.isChecked():
            modif.time_type = TimeType.NoneTime
        elif self.ui.radioButton_CustomTime.isChecked():
            modif.time_type = TimeType.CustomTime
        elif self.ui.radioButton_CreateTime.isChecked():
            modif.time_type = TimeType.CreatTime
        elif self.ui.radioButton_ForceTime.isChecked():
            modif.time_type = TimeType.ForceTime
        modif.modifDirAllFile()

    def onProcessMessage(self, value):
        self.ui.textEdit.append(value)

    # 选择一个文件
    def selectFile(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.exec()
        # 获取选择的文件路径
        path = dialog.selectedFiles()[0]
        # 显示选择的文件路径
        self.ui.lineEdit_FilePath.setText(path)

    def startModifFile(self):
        # 获取选择的文件路径
        path = self.ui.lineEdit_FilePath.text()
        if path == "":
            QMessageBox.information(self, "提示", "请选择一个文件")
            return
        if self.ui.lineEdit_FileCustomTime.text() == "":
            QMessageBox.information(self, "提示", "请输入时间")
            return
        # 检查时间格式是否正确 "%Y:%m:%d %H:%M:%S"
        if not self.checkTimeFormat(self.ui.lineEdit_FileCustomTime.text(),time_format):
            QMessageBox.information(self, "提示", "时间格式不正确")
            return
        writeTime(path, self.ui.lineEdit_FileCustomTime.text())
        self.ui.textEdit.append(path + " --> " +self.ui.lineEdit_FileCustomTime.text())

    def checkTimeFormat(self, timeStr, time_format):
        try:
            time.strptime(timeStr, time_format)
            return True
        except ValueError:
            return False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 设置界面风格，这里使用 "Fusion" 风格
    app.setStyle(QStyleFactory.create("fusion"))
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
