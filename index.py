
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow

import sys
from player import Player

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    window = Player()
   
    window.show()
    sys.exit(app.exec_())
