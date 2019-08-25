import sys
from PyQt4 import QtGui, QtCore

print(sys.argv)
class Window(QtGui.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.width = 500
        self.height = 400
        self.setGeometry(450,300,self.width,self.height)
        self.setWindowTitle('My Window')
        self.setWindowIcon(QtGui.QIcon('icon16.ico'))

        #main menu
        exit_me = QtGui.QAction('&Exit me', self)
        exit_me.setShortcut('Ctrl+Q')
        #status bar on pointer
        exit_me.setStatusTip('Leave the App')
        #clicked
        exit_me.triggered.connect(self.close_me)

        #editor
        openeditor = QtGui.QAction('&Editor', self)
        openeditor.setShortcut('Ctrl+E')
        openeditor.setStatusTip('Open editor')
        openeditor.triggered.connect(self.open_editor)

        #open file
        openFile = QtGui.QAction('&Open file', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open file')
        openFile.triggered.connect(self.open_file)
        
        #save file
        saveFile = QtGui.QAction('&Save file', self)
        saveFile.setShortcut('Ctrl+S')
        saveFile.setStatusTip('Save file')
        saveFile.triggered.connect(self.save_file)


        #create status bar
        self.statusBar()

        #create mainmenu panel
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(exit_me)
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)
        
        editorMenu = mainMenu.addMenu('&Editor')
        editorMenu.addAction(openeditor)

        #run
        self.home()

    def home(self):
        btn_width = 100
        btn_height = 30

        #label
        self.showstyle = QtGui.QLabel('Windows Vista', self)
        #align label
        self.showstyle.setAlignment(QtCore.Qt.AlignCenter)
        self.showstyle.move(120,70)

        #create buttons
        btn1 = QtGui.QPushButton('Quit', self)
        btn1.clicked.connect(self.close_me)
        #resize(100,30),(optimal size)
        btn1.resize(btn1.sizeHint())
        #move buttons
        btn1.move((self.width-btn_width)//2+50, 73)

        #toolbar
        mytoolbar  = QtGui.QAction(QtGui.QIcon('tavern.png'), 'I am tavern', self)
        mytoolbar.triggered.connect(self.close_me)
        #create toolbar
        self.toolBar = self.addToolBar('drink')
        self.toolBar.addAction(mytoolbar)


        #font choice
        fontchoice  = QtGui.QAction('Label font', self)
        fontchoice.triggered.connect(self.font_choice)
        #add to toolbar
        self.toolBar = self.addToolBar('font')
        self.toolBar.addAction(fontchoice)

        #font colour choice
        color = QtGui.QColor(100,100,100)
        
        fontcolor = QtGui.QAction('Label colour', self)
        fontcolor.triggered.connect(self.color_picker)

        #make toolbar distinctive
        #self.toolBar = self.addToolBar('I am color font')
        self.toolBar.addAction(fontcolor)


        #checkbox
        checkbox = QtGui.QCheckBox('Enlarge me', self)
        checkbox.move(self.width-100,70)
        #autochecked
        #checkbox.toggle()
        
        #assign change
        checkbox.stateChanged.connect(self.enlarge_me)

        #progress bar
        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(100,150, 180,20)
        self.progress.move(15,120)

        btn3 = QtGui.QPushButton('Download', self)
        btn3.resize(btn3.sizeHint())
        btn3.move(60,150)
        btn3.clicked.connect(self.download)


        #combo box
        combobox = QtGui.QComboBox(self)
        combobox.addItem('motif')
        combobox.addItem('Windows')
        combobox.addItem('cde')
        combobox.addItem('Plastique')
        combobox.addItem('Cleanlooks')
        combobox.addItem('windowsvista')
        combobox.move(5,70)
        
        #activating and passing argument
        combobox.activated[str].connect(self.style_choice)


        #calendar
        cal = QtGui.QCalendarWidget(self)
        cal.move(200,120)
        cal.resize(250,200)

        self.style_choice('Plastique')
        self.show()


    def open_editor(self):
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)

    def open_file(self):
        name = QtGui.QFileDialog.getOpenFileName(self, 'Open file')
        file = open(name, 'r')
        self.open_editor()
        with file:
            text = file.read()
            self.textEdit.setText(text)

    def save_file(self):
        name = QtGui.QFileDialog.getSaveFileName(self, 'Save file')
        with open(name, 'w') as file:
            text = self.textEdit.toPlainText()
            file.write(text)

    def color_picker(self):
        color = QtGui.QColorDialog.getColor()
        #customise things within application
        self.showstyle.setStyleSheet('QWidget { background-color: %s}' % color.name())

    def style_choice(self, text):
        self.showstyle.setText(text)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))

    def font_choice(self):
        font, valid = QtGui.QFontDialog.getFont()
        if valid:
            self.showstyle.setFont(font)


    def enlarge_me(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(150,100, 1000,600)
        else:
            self.setGeometry(450, 300, self.width, self.height)

    def download(self):
        self.completed = 0
        while self.completed < 100:
            self.completed += 0.00005
            self.progress.setValue(self.completed)

    def close_me(self):
        my_choice = QtGui.QMessageBox.question(self, 'Go home Laowai',
                                               'Ready to dispatch?',
                                               QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if my_choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass
        




def run():
    app = QtGui.QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()
