from PyQt5.QtWidgets import QFrame
from ui.wf_ksrm import Ui_wf_ksrm
from PyQt5.QtCore import Qt

class init_window_ksrm:
    def __init__(self, window: QFrame, ui: Ui_wf_ksrm,x,y,typeText,tpyeKJ,docText):
        self.window = window
        self.ui = ui
        self.x = x
        self.y = y
        self.typeText=typeText
        self.tpyeKJ = tpyeKJ
        self.docText=docText
        self.set()
    def set(self):
        # 设置标题
        if self.tpyeKJ=='ksrm':
            typeTitle="快速入门"
        elif self.tpyeKJ=='scbd':
            typeTitle = "速查宝典"
        self.window.setWindowTitle(self.typeText+typeTitle)
        # 设置窗口无边框,和透明背景
        self.window.move(self.x, self.y)
        self.window.setWindowFlags(Qt.WindowMaximizeButtonHint  | Qt.FramelessWindowHint)
        self.window.setAttribute(Qt.WA_TranslucentBackground)  # 窗口透明
        # 如果设置True,则支持弹出浏览器访问链接  反之则只能调用槽函数
        self.ui.lb_doc.setOpenExternalLinks(True)
        self.ui.lb_doc.setText(self.docText)
        self.window.adjustSize()
        self.window.resize(self.window.width()+10,self.window.height())

