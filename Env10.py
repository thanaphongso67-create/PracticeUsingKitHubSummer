import sys
from PySide6.QtWidgets import *

class myMessageBox(QWidget):
    def __init__(self, parent=None):
        # เรียกใช้งานคอนสตรัคเตอร์ของ QWidget
        super().__init__(parent)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('กล่องข้อความ') # ชื่อหัวของโปรแกรม

    # ฟังก์ชันตรวจสอบเหตุการณ์การปิดหน้าต่าง
    def closeEvent(self, event): 
        # สร้างกล่องคำถามถามผู้ใช้
        reply = QMessageBox.question(self, 'Message',
                                   "คุณแน่ใจนะว่าคุณต้องการปิดโปรแกรม?", 
                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept() # ยืนยันการปิดโปรแกรม
        else:
            event.ignore() # ยกเลิกการปิด (โปรแกรมยังทำงานต่อ)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # สร้าง Object จากคลาส myMessageBox
    qb = myMessageBox() 
    qb.show() 
    
    sys.exit(app.exec())