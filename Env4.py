import sys
from PySide6.QtWidgets import *

class myApp(QWidget):
    def __init__(self):
        super().__init__()
        # 1. ตั้งค่าหน้าต่างหลัก
        self.resize(320, 240) 
        self.setWindowTitle("Hello, World!") 

        # 2. สร้าง Layout และ Widgets
        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel("Hello World")
        layout.addWidget(label) # เพิ่ม Label เข้าไปใน Layout

# --- ส่วนการรันโปรแกรม ---
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    win = myApp() # สร้าง Object จาก Class ที่เราเขียน
    win.show()    # สั่งให้หน้าต่างแสดงผล
    
    sys.exit(app.exec())