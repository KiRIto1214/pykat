import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
class MainWindow(QMainWindow) :

    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #nav
        nav = QToolBar()
        self.addToolBar(nav)

        back_btn = QAction('----', self)
        back_btn.triggered.connect(self.browser.back)
        nav.addAction(back_btn)

        forward_btn = QAction('++++', self)
        forward_btn.triggered.connect(self.browser.forward)
        nav.addAction(forward_btn)

        reload_btn = QAction('====', self)
        reload_btn.triggered.connect(self.browser.reload)
        nav.addAction(reload_btn)

        home_page = QAction('[  *  ]',self)
        home_page.triggered.connect(self.navigate_home)
        nav.addAction(home_page)

        youtube = QAction('U_T_B', self)
        youtube.triggered.connect(self.you_tube)
        nav.addAction(youtube)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_tourl)
        nav.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):

        self.browser.setUrl(QUrl('https://bing.com'))

    def navigate_tourl(self):
        url = self.url_bar.text()
        self.browser.setUrl((QUrl(url)))

    def update_url(self, w):
        self.url_bar.setText(w.toString())

    def you_tube(self):
        self.browser.setUrl(QUrl('https://youtube.com'))


app = QApplication(sys.argv)
QApplication.setApplicationName('Krypton')

window = MainWindow()

app.exec_()