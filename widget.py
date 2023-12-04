# This Python file uses the following encoding: utf-8
import sys
import os
import piexif
from win32file import CreateFile, SetFileTime, GetFileTime, CloseHandle
from win32file import GENERIC_READ, GENERIC_WRITE, OPEN_EXISTING
from pywintypes import Time # 可以忽视这个 Time 报错（运行程序还是没问题的）
import time



class ModifTime2ShootTime:
    def __init__(self, path):
        self.dir_path = path
        self.current_file_path = ""
        self.current_file_time = ""
        self.custom_file_time = "" # 如果没有获取到时间，则使用默认时间

    def modifDirAllFile(self):
        file_name_list = os.listdir(self.dir_path)
        # 从文件夹中获取文件文件
        for file_name in file_name_list:
            if not file_name.endswith(".JPG"):
                continue
            # 生成具体文件路径
            self.current_file_path = self.dir_path + file_name
            print(self.current_file_path)
            # 提取拍摄时间
            self.readShootTime()
            print(self.current_file_time)
            # 写入到 创建时间 修改时间 访问时间
            writeTime(self.current_file_path, self.custom_file_time)

            # 休息一下，防止太快
            time.sleep(0.01)

    def readShootTime(self):
        exif_dict = piexif.load(self.current_file_path)
        # 尝试获取拍摄时间，如果没有获取到，则使用自定义时间
        try:
            time_str = str(exif_dict["Exif"][36868])
            self.current_file_time = time_str[2:len(time_str) - 1]
        except:
            self.current_file_time = self.custom_file_time


def timeOffsetAndStruct(times, format, offset):
  return time.localtime(time.mktime(time.strptime(times, format)) + offset)

def writeTime(file_path,file_times):
    format = "%Y:%m:%d %H:%M:%S"  # 时间格式
    # 进行时间偏移 1S，避免创建时间，修改时间，访问时间都一样
    cTime_t = timeOffsetAndStruct(file_times, format, 0)
    mTime_t = timeOffsetAndStruct(file_times, format, 1)
    aTime_t = timeOffsetAndStruct(file_times, format, 2)

    fh = CreateFile(file_path, GENERIC_READ | GENERIC_WRITE, 0, None, OPEN_EXISTING, 0, 0)

    createTimes, accessTimes, modifyTimes = GetFileTime(fh)
    createTimes = Time(time.mktime(cTime_t))
    accessTimes = Time(time.mktime(aTime_t))
    modifyTimes = Time(time.mktime(mTime_t))
    SetFileTime(fh, createTimes, accessTimes, modifyTimes)
    CloseHandle(fh)



from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
