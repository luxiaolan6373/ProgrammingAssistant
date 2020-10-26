from PyQt5.QtWidgets import QMainWindow
from ui.wf_main import Ui_MainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
import time


class init_window_main:
    def __init__(self, window: QMainWindow, ui: Ui_MainWindow):
        self.window = window
        self.ui = ui
        self.x = -70
        self.y = 0
        self.set()

    def set(self):
        # 设置标题
        self.window.setWindowTitle('python懒人工具www.52pojie.cn')
        # 设置窗口无边框,和透明背景

        self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.ui.frame_main.setContentsMargins(0, 0, 0, 0)
        self.window.move(self.x, self.y)
        self.window.setWindowFlags(Qt.WindowMaximizeButtonHint | Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.window.setAttribute(Qt.WA_TranslucentBackground)  # 窗口透明
        # 设置鼠标为手型
        self.window.setCursor(QCursor(Qt.PointingHandCursor))
        # 设置toolTip
        self.ui.bt_python.setToolTip("python的基础教程以工具")
        self.ui.bt_spider.setToolTip("python爬虫基础和工具")
        self.ui.bt_pyQt5.setToolTip("pythonGUI中最牛的ui设计库的学习和便民工具")
        self.ui.bt_dm.setToolTip("python开发windows开发脚本必备插件(收费的)")
        self.ui.bt_lw.setToolTip("python开发windows开发脚本必备插件(免费的)")
        self.ui.bt_win32.setToolTip("python对接windowsAPI必备资料")
        self.ui.bt_flask.setToolTip("python开发web服务器后端,api接口编写")
        # 隐藏子功能按钮
        self.ui.frame_python.setVisible(False)
        self.ui.frame_spider.setVisible(False)
        self.ui.frame_pyQt5.setVisible(False)
        self.ui.frame_dm.setVisible(False)
        self.ui.frame_lw.setVisible(False)
        self.ui.frame_win32.setVisible(False)
        self.ui.frame_flask.setVisible(False)

        # 绑定信号绑定槽---主界面的动画效果
        self.ui.frame_main.enterEvent = self.enterEvent
        self.ui.frame_main.leaveEvent = self.leaveEvent

        #展开和隐藏具体栏目的信号绑定槽
        self.ui.bt_python.clicked.connect(self.clicked)
        self.ui.bt_spider.clicked.connect(self.clicked)
        self.ui.bt_pyQt5.clicked.connect(self.clicked)
        self.ui.bt_dm.clicked.connect(self.clicked)
        self.ui.bt_lw.clicked.connect(self.clicked)
        self.ui.bt_win32.clicked.connect(self.clicked)
        self.ui.bt_flask.clicked.connect(self.clicked)

    def enterEvent(self, event):
        '''
        鼠标进入主界面时触发
        :param event:
        :return:
        '''
        if self.window.x() == self.x:
            for i in range(abs(self.x )):
                self.window.move(self.x + i+1, self.y)
                time.sleep(0.0015)
            print('进入')
        print(self.window.x())

    def leaveEvent(self, event):
        '''
        鼠标离开主界面时触发
        :param event:
        :return:
        '''
        x = 0

        tj = self.ui.frame_python.isVisible() == False and self.ui.frame_spider.isVisible() == False and self.ui.frame_pyQt5.isVisible() == False and self.ui.frame_dm.isVisible() == False and self.ui.frame_lw.isVisible() == False and self.ui.frame_win32.isVisible() == False and self.ui.frame_flask.isVisible()==False
        print(tj )
        if self.window.x() == x and tj == True:
            for i in range(abs(self.x - x)):
                self.window.move(x - i - 1, self.y)
                time.sleep(0.0015)
            print('离开')
    def clicked(self):
        '''
        鼠标点击某个栏目时触发
        :return:
        '''
        item=self.window.sender()
        #取出目标功能框架
        if item.text()=='python':
            f =self.ui.frame_python
        elif item.text()=='爬虫':
            f = self.ui.frame_spider
        elif item.text()=='PyQt5':
            f=self.ui.frame_pyQt5
        elif item.text()=='大漠':
            f=self.ui.frame_dm
        elif item.text()=='乐玩':
            f=self.ui.frame_lw
        elif item.text()=='win32':
            f=self.ui.frame_win32
        elif item.text()=='flask':
            f=self.ui.frame_flask
        #设置显示或者隐藏框架
        if f.isVisible()==False:
            self.ui.frame_python.setVisible(False)
            self.ui.frame_spider.setVisible(False)
            self.ui.frame_pyQt5.setVisible(False)
            self.ui.frame_dm.setVisible(False)
            self.ui.frame_lw.setVisible(False)
            self.ui.frame_win32.setVisible(False)
            self.ui.frame_flask.setVisible(False)
            f.setVisible(True)

        else:
            f.setVisible(False)
        print('点击:',item.text())

