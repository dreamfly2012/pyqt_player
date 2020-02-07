from UI_player import Ui_Form
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent,QMediaPlaylist
from PyQt5.Qt import QUrl,QDir
from PyQt5.QtWidgets import QMainWindow,QFileDialog

class Player(QMainWindow,Ui_Form):
    def __init__(self, parent=None):
        super(Player, self).__init__()
        self.setupUi(self)
        self.playlist = QMediaPlaylist()
        #self.UI_Form.playbtn.clicked.connect(self.play)
        #self.stopbtn.clicked.connect(self.stop)
        
        



    #初始化播放器列表
    def init_playlist(self,filename):
        self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(filename)))
        self.playlist.setCurrentIndex(1)
        self.start()

    #初始化播放器
    def start(self):
        self.player = QMediaPlayer()
        #self.player = QMediaPlayer(self)            # 1
        #self.media_content = QMediaContent(QUrl.fromLocalFile('D:/code/qifengle.mp3'))  # 2
        # self.player.setMedia(QMediaContent(QUrl('http://example.com/music.mp3')))
        #self.player.setMedia(self.media_content)    # 3

        self.player.setPlaylist(self.playlist)
        self.player.setVolume(5)
         
        
    #控制播放，暂停
    def play(self):
        if self.player.state() == 0 or self.player.state() == 2:
            self.player.play()
            self.playbtn.setText("播放")
        else:
            self.player.pause()
            self.playbtn.setText("暂停")        
        pass
    
    #控制打开文件夹
    def fileopen(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        
        
		
        if dlg.exec_():
            filenames = dlg.selectedFiles()
            filename = filenames[0]
            self.init_playlist(filename)
			
        # with f:
        #     data = f.read()
        #     self.contents.setText(data)

    

    def valuechanged(self):
        currentValue = self.horizontalSlider.value()
        self.player.setVolume(currentValue)




    
    def self_func(self):
        pass