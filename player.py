from UI_player import Ui_Form
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent,QMediaPlaylist
from PyQt5.Qt import QUrl,QDir
from PyQt5.QtWidgets import QMainWindow,QFileDialog,QMessageBox
from PyQt5.QtCore import QStringListModel
import os

class Player(QMainWindow,Ui_Form):
    def __init__(self, parent=None):
        super(Player, self).__init__()
        self.setupUi(self)
        self.player = QMediaPlayer()
        self.currentIndex = 1
        self.cwd = os.getcwd() # 获取当前程序文件位置
        self.qList = []
        self.playlist = QMediaPlaylist()
        self.listView.clicked.connect(self.clickedlist)		 #listview 的点击事件 
        #self.UI_Form.playbtn.clicked.connect(self.play)
        #self.stopbtn.clicked.connect(self.stop)
        
        
    #播放器列表添加
    def add_playlist(self, filename):
        self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(filename)))

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
        self.play()
         
        
    #控制播放，暂停
    def play(self):
        if self.player.state() == 0 or self.player.state() == 2:
            self.player.play()
            self.playbtn.setText("||")
        else:
            self.player.pause()
            self.playbtn.setText("△")        
        pass
    
    #控制打开文件夹
    def fileopen(self):
        files, filetype = QFileDialog.getOpenFileNames(self,  
                                    "多文件选择",  
                                    self.cwd, # 起始路径 
                                    "MP3 Files (*.mp3)")  

        if len(files) == 0:
            print("\n取消选择")
            return

        print("\n你选择的文件为:")

        
        for file in files:
            
            self.qList.append(file)
            
            self.add_playlist(file)
            print(file)
        
        self.player.setPlaylist(self.playlist)
        model = QStringListModel(); #创建mode
        #self.qList = ['Item 1','Item 2','Item 3','Item 4' ]	 #添加的数组数据
        model.setStringList(self.qList) #将数据设置到model
        self.listView.setModel(model)##绑定 listView 和 model
           
        print("文件筛选器类型: ",filetype)



        # dlg = QFileDialog()
        # dlg.setFileMode(QFileDialog.AnyFile)
        
        
		
        # if dlg.exec_():
        #     filenames = dlg.selectedFiles()
        #     filename = filenames[0]
        #     self.init_playlist(filename)
			
        # with f:
        #     data = f.read()
        #     self.contents.setText(data)

    #上一首
    def prev(self):
        self.playlist.previous()
        #self.currentIndex = self.playlist.previousIndex()
        #self.playlist.setCurrentIndex(self.currentIndex)
        self.player.play()

    #下一首
    def next(self):
        self.playlist.next()
        #self.currentIndex = self.playlist.nextIndex()
        #self.playlist.setCurrentIndex(self.currentIndex)
        self.player.play()
        pass
   

    def clickedlist(self, qModelIndex):
        #QMessageBox.information(self, "QListView", "你选择了: "+ self.qList[qModelIndex.row()])
        index = qModelIndex.row()  
        self.currentIndex = index+1
        self.playlist.setCurrentIndex(self.currentIndex)
        self.player.play()
        print("点击的是：" + str(qModelIndex.row()))
    

    

    def valuechanged(self):
        currentValue = self.horizontalSlider.value()
        self.player.setVolume(currentValue)




    
    def self_func(self):
        pass