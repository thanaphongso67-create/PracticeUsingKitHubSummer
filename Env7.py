import sys
from PySide6.QtWidgets import *
from PySide6.QtWebEngineWidgets import QWebEngineView

class myWeb(QWebEngineView):
    def __init__(self):
        super().__init__()
        try:
            # อ่านไฟล์รูปภาพในโหมด binary ('rb')
            # ตรวจสอบให้แน่ใจว่าไฟล์ '101_0336.png' อยู่ในโฟลเดอร์เดียวกับไฟล์ .py นี้
            img = open('101_0336.png', 'rb').read() 
            
            # แสดงเนื้อหาโดยกำหนด MIME type เป็น image/png
            # หมายเหตุ: ชื่อฟังก์ชันต้องเขียนติดกันคือ setContent
            self.setContent(img, "image/png")
            
            self.resize(800, 600)
            self.setWindowTitle("Image Display Test")
        except FileNotFoundError:
            print("Error: ไม่พบไฟล์ 101_0336.png ในโฟลเดอร์ของโปรเจกต์")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    web = myWeb()
    web.show()
    
    sys.exit(app.exec())