from UI_player import Ui_Form
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.Qt import QUrl

class Player(Ui_Form):
    def __init__(self, parent=None):
        super(Player, self).__init__()
        
        self.player = QMediaPlayer()
        #self.player = QMediaPlayer(self)            # 1
        self.media_content = QMediaContent(QUrl.fromLocalFile('D:/code/qifengle.mp3'))  # 2
        # self.player.setMedia(QMediaContent(QUrl('http://example.com/music.mp3')))
        self.player.setMedia(self.media_content)    # 3
        self.player.setVolume(80)                   # 4
        self.player.play()
    
    def self_func(self):
        pass