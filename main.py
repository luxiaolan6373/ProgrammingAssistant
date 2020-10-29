from PyQt5.QtWidgets import QApplication,QMainWindow
from ui import wf_main
from code_ui.code_main import init_window_main
import sys,subprocess

if __name__ == '__main__':
    app=QApplication(sys.argv)
    window_main = QMainWindow()  # 主界面
    ui_main=wf_main.Ui_MainWindow()#实例化
    ui_main.setupUi(window_main)#运行里面的代码
    init_window_main(window_main,ui_main)#初始化和对接代码功能
    window_main.show()
    sys.exit(app.exec_())



