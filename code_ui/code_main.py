from PyQt5.QtWidgets import QMainWindow,QFrame,QApplication,qApp
from ui.wf_main import Ui_MainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor,QIcon
from code_ui.code_ksrm import init_window_ksrm
from ui import wf_ksrm
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
import time,os


class init_window_main:
    def __init__(self, window: QMainWindow, ui: Ui_MainWindow):
        self.window = window
        self.ui = ui
        self.x = -70
        self.y = 0

        self.set()
        self.path=os.getcwd()

    def set(self):
        # 设置标题
        self.window.setWindowTitle('python懒人工具www.52pojie.cn')
        self.window.setWindowIcon(QIcon('logo.ico'))
        # 设置窗口无边框,和透明背景
        self.ui.frame_main_hb.setContentsMargins(0, 0, 0, 0)
        self.ui.frame_main.setContentsMargins(0, 0, 0, 0)
        self.window.move(self.x, self.y)
        self.window.setWindowFlags(Qt.WindowMaximizeButtonHint | Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.window.setAttribute(Qt.WA_TranslucentBackground)  # 窗口透明
        # 设置鼠标为手型
        self.window.setCursor(QCursor(Qt.PointingHandCursor))
        # 设置toolTip
        self.ui.bt_python.setToolTip("python的基础教程和工具,资料全部来自互联网")
        self.ui.bt_spider.setToolTip("python爬虫基础和工具,资料全部来自互联网")
        self.ui.bt_pyQt5.setToolTip("pythonGUI中最牛的ui设计库的学习和便民工具,资料全部来自互联网")
        self.ui.bt_dm.setToolTip("python开发windows开发脚本必备插件(收费的),资料全部来自互联网")
        self.ui.bt_lw.setToolTip("python开发windows开发脚本必备插件(免费的),资料全部来自互联网")
        self.ui.bt_win32.setToolTip("python对接windowsAPI必备资料,资料全部来自互联网")
        self.ui.bt_webkj.setToolTip("python开发web服务器后端,api接口编写,资料全部来自互联网")

        self.ui.bt_python_scbd.setToolTip('里面有个搜索框,快速搜索,这是官方的中文帮助,没有比这更全面的了,搜索有点慢,慢慢翻一定可以搜到')
        self.ui.bt_python_gnhs.setToolTip('收集的一些常用封装好的功能性函数,直接复制粘贴岂不快哉!')
        self.ui.bt_spider_jsonjx.setToolTip('超好用的json解析工具')
        self.ui.bt_spider_zbgj.setToolTip('全网公认最好用的抓包工具Fiddler,可以抓手机电视等只要联网的设备的包')
        self.ui.bt_pyQt5_qssgj.setToolTip('全网公认最好用的QSS可视化编辑神器,不要太好用喔,哈哈')
        self.ui.bt_win32_apizs.setToolTip('易语言官方的api中文助手:有一定python win32基础后用这个搜索api功能非常方便!')
        self.ui.bt_win32_jyzs.setToolTip('精易编程助手:功能有查看窗口信息,抓包,翻译,取色,正则表达式等都有.稍微代码转换一下到python就行了!')
        # 隐藏子功能按钮
        self.ui.frame_python.setVisible(False)
        self.ui.frame_spider.setVisible(False)
        self.ui.frame_pyQt5.setVisible(False)
        self.ui.frame_dm.setVisible(False)
        self.ui.frame_lw.setVisible(False)
        self.ui.frame_win32.setVisible(False)
        self.ui.frame_webkj.setVisible(False)

        # 重写事件---主界面的动画效果
        self.ui.frame_main.enterEvent = self.enterEvent
        self.ui.frame_main.leaveEvent = self.leaveEvent

        #展开和隐藏具体栏目的信号绑定槽
        self.ui.bt_python.clicked.connect(self.clicked)
        self.ui.bt_spider.clicked.connect(self.clicked)
        self.ui.bt_pyQt5.clicked.connect(self.clicked)
        self.ui.bt_dm.clicked.connect(self.clicked)
        self.ui.bt_lw.clicked.connect(self.clicked)
        self.ui.bt_win32.clicked.connect(self.clicked)
        self.ui.bt_webkj.clicked.connect(self.clicked)
        #关闭按钮

        self.ui.bt_gb.clicked.connect(qApp.exit)
        #快速入门具体功能按钮的信号绑定槽 因为 用lambad表达式传参数
        self.ui.bt_python_ksrm.clicked.connect(lambda: self.clicked_ksrm(self.ui.frame_python,'python','ksrm'))
        self.ui.bt_spider_ksrm.clicked.connect(lambda: self.clicked_ksrm(self.ui.frame_spider,'spider','ksrm'))
        self.ui.bt_pyQt5_ksrm.clicked.connect(lambda: self.clicked_ksrm(self.ui.frame_pyQt5,'pyQt5','ksrm'))
        self.ui.bt_dm_ksrm.clicked.connect(lambda: self.clicked_ksrm(self.ui.frame_dm,'dm','ksrm'))
        self.ui.bt_lw_ksrm.clicked.connect(lambda: self.clicked_ksrm(self.ui.frame_lw,'lw','ksrm'))
        self.ui.bt_win32_ksrm.clicked.connect(lambda: self.clicked_ksrm(self.ui.frame_win32,'win32','ksrm'))
        self.ui.bt_webkj_ksrm.clicked.connect(lambda: self.clicked_ksrm(self.ui.frame_webkj,'webkj','ksrm'))
        #速查宝典start是不等待执行结束
        self.ui.bt_lw_scbd.clicked.connect(lambda: os.system(f'start hh {self.path}\html\lw\乐玩插件接口说明.chm'))
        self.ui.bt_dm_scbd.clicked.connect(lambda: os.system(f'start hh {self.path}\html\dm\大漠插件接口说明.chm'))
        self.ui.bt_win32_scbd.clicked.connect(lambda: os.system(f'start hh {self.path}/html/win32/PyWin32.chm ' ))
        self.ui.bt_python_scbd.clicked.connect(lambda: QDesktopServices.openUrl(QUrl("https://docs.python.org/zh-cn/3/")))
        self.ui.bt_spider_scbd.clicked.connect(lambda: self.clicked_ksrm(self.ui.frame_spider,'spider', 'scbd'))
        self.ui.bt_webkj_scbd.clicked.connect(lambda: self.clicked_ksrm(self.ui.frame_webkj,'webkj', 'scbd'))

        #大漠综合工具
        self.ui.bt_dm_zhgj.clicked.connect(lambda: os.system(f'start {self.path}\html\dm\综合工具\大漠综合工具.exe'))
        #大漠绑定工具
        self.ui.bt_dm_bdgj.clicked.connect(lambda: os.system(f'start {self.path}\html\dm\绑定工具\大漠插件绑定测试工具(VIP专用).exe'))
        # 乐玩编程助手
        self.ui.bt_lw_lwzs.clicked.connect(lambda: os.system(f'start {self.path}\html\lw\编程助手\乐玩助手.exe'))
        #fiddler抓包工具
        self.ui.bt_spider_zbgj.clicked.connect(lambda: os.system(f'start {self.path}\html\spider\Fiddler\Fiddler.exe'))
        #JSONG解析
        self.ui.bt_spider_jsonjx.clicked.connect(lambda: QDesktopServices.openUrl(QUrl("https://www.bejson.com/jsonviewernew/")))
        # Qss工具
        pythonPath = f'\html\pyQt5\QssStylesheetEditor\libpython\pythonw.exe'
        exePath = f'\html\pyQt5\QssStylesheetEditor\scripts\main.pyc'
        self.ui.bt_pyQt5_qssgj.clicked.connect(lambda: os.system(f'start {self.path}{pythonPath} {self.path}{exePath}'))
        #功能函数
        self.ui.bt_python_gnhs.clicked.connect(lambda: QDesktopServices.openUrl(QUrl("http://012.plus/static/pyec/iframe/index.html#/pyec/wangye")))

        # api中文助手
        self.ui.bt_win32_apizs.clicked.connect(lambda: os.system(f'start {self.path}\html\win32\\apiZhuShou\API助手.exe'))
        #精易编程助手
        self.ui.bt_win32_jyzs.clicked.connect(lambda: os.system(f'start {self.path}\html\win32\精易编程助手\精易编程助手.exe'))




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

        tj = self.ui.frame_python.isVisible() == False and self.ui.frame_spider.isVisible() == False and self.ui.frame_pyQt5.isVisible() == False and self.ui.frame_dm.isVisible() == False and self.ui.frame_lw.isVisible() == False and self.ui.frame_win32.isVisible() == False and self.ui.frame_webkj.isVisible()==False
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
        elif item.text()=='web框架':
            f=self.ui.frame_webkj
        #设置显示或者隐藏框架
        if f.isVisible()==False:
            self.ui.frame_python.setVisible(False)
            self.ui.frame_spider.setVisible(False)
            self.ui.frame_pyQt5.setVisible(False)
            self.ui.frame_dm.setVisible(False)
            self.ui.frame_lw.setVisible(False)
            self.ui.frame_win32.setVisible(False)
            self.ui.frame_webkj.setVisible(False)
            f.setVisible(True)

        else:
            f.setVisible(False)
        print('点击:',item.text())
    def clicked_ksrm(self,item_fram,typeText,typeKJ):
        '''快速入门窗口的展示'''
        #根据返回的类型来创建不一样的窗口
        self.window_ksrm = QFrame()
        self.ui_ksrm = wf_ksrm.Ui_wf_ksrm()
        self.ui_ksrm.setupUi(self.window_ksrm)
        with open(f'html/{typeText}/{typeKJ}.html', 'r', encoding='utf-8')as f:
            docText = f.read()
        init_window_ksrm(self.window_ksrm, self.ui_ksrm, item_fram.x() + item_fram.width() - 8,
                         self.ui.frame_python.y(), typeText,typeKJ,docText)
        self.window_ksrm.show()

