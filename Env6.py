import sys
from PySide6.QtWidgets import *
from PySide6.QtWebEngineWidgets import QWebEngineView

class myWeb(QWebEngineView):
    def __init__(self):
        super().__init__()
        # กำหนดเนื้อหา HTML
        self.setHtml('''<html>
            <head>
                <title>ทดสอบ</title>
            </head>
            <body>
                <h1>Hello, World!</h1>
                <hr />
                <p>ทดสอบการแสดงผล HTML ใน QWebView</p>
            </body>
        </html>''')
        self.resize(600, 400) # กำหนดขนาดหน้าต่างให้เหมาะสม
        self.setWindowTitle("HTML Display Test")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    web = myWeb()
    web.show()
    
    sys.exit(app.exec())