import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
app = QApplication(sys.argv)
quit = QPushButton("Quit") #กาํหนดขอ้ความในปุ่ม
quit.resize(75, 30) #กาํหนดขนาดของปุ่ม
quit.setFont(QFont("Times", 18,QFont.Bold))
QObject.connect(quit,SIGNAL("clicked()"),
app, SLOT("quit()"))
quit.show()
sys.exit(app.exec_())