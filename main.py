import sys
from PySide6.QtWidgets import QApplication

from classdefs.modmainwindow import NemoMainWindow


app = QApplication(sys.argv)
app.setStyle('Fusion')
window = NemoMainWindow()
window.show()
app.exec()

print('hello')
