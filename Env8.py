import sys
from PySide6.QtWidgets import *

class myApp(QWidget):
    def __init__(self):
        super().__init__()
        # 1. กำหนดขนาดหน้าต่างและชื่อหัวโปรแกรม
        self.resize(320, 240) 
        self.setWindowTitle("Hello, World!") 

        # 2. สร้าง Layout เพื่อจัดวางวัตถุ
        layout = QVBoxLayout()
        self.setLayout(layout)

        # 3. สร้างปุ่มกดและเพิ่มเข้าไปใน Layout
        hello = QPushButton("Hello world!") 
        # หมายเหตุ: เมื่อใช้ Layout ขนาดปุ่มจะถูกปรับอัตโนมัติตาม Layout
        hello.setFixedSize(100, 30) # ใช้ setFixedSize เพื่อคุมขนาดปุ่มให้คงที่
        layout.addWidget(hello)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    win = myApp()
    win.show()
    
    sys.exit(app.exec())