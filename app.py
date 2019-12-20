from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QTextEdit, QLineEdit, \
    QComboBox, QMenuBar, QMenu, QAction
import sys




class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle("DDOS Detector")
        self.resize(800, 600)
        self.Componnent()
        self.show()

    def Componnent(self):

        self.label = QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 20, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.lineEdit = QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(100, 30, 561, 32))
        font = QtGui.QFont()
        font.setPointSize(12)

        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")

        self.btnBrowse = QPushButton(self)
        self.btnBrowse.setGeometry(QtCore.QRect(680, 30, 88, 34))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnBrowse.setFont(font)
        self.btnBrowse.setObjectName("btnBrowse")

        self.comboBox = QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(100, 80, 271, 32))
        self.comboBox.setObjectName("comboBox")

        self.label_3 = QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(320, 150, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.image = QLabel(self)
        self.image.setGeometry(QtCore.QRect(350, 300, 58, 18))
        self.image.setObjectName("image")

        self.btnReport = QPushButton(self)
        self.btnReport.setGeometry(QtCore.QRect(310, 510, 171, 34))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnReport.setFont(font)
        self.btnReport.setObjectName("btnReport")

        self.btnCalculation = QPushButton(self)
        self.btnCalculation.setGeometry(QtCore.QRect(510, 510, 231, 34))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnCalculation.setFont(font)
        self.btnCalculation.setObjectName("btnCalculation")

        self.menubar = QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 30))
        self.menubar.setObjectName("menubar")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")

        self.actionOpen = QAction(self)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QAction(self)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QAction(self)
        self.actionAbout.setObjectName("actionAbout")
        self.actionUsage = QAction(self)
        self.actionUsage.setObjectName("actionUsage")

        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionUsage)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.label.setText("Filename")
        self.label_2.setText("Server IP")
        self.btnBrowse.setText("Browse")
        self.label_3.setText("Scan Result")
        self.image.setText("image")
        self.btnReport.setText("View Scan Report")
        self.btnCalculation.setText("View Calculation Report")
        self.menuFile.setTitle("File")
        self.menuHelp.setTitle("Help")
        self.actionOpen.setText("Open")
        self.actionOpen.setShortcut("Ctrl+O")
        self.actionExit.setText("Exit")
        self.actionExit.setShortcut("Alt+F4")
        self.actionAbout.setText("About")
        self.actionAbout.setShortcut("Ctrl+A")
        self.actionUsage.setText("Usage")
        self.actionUsage.setShortcut("Ctrl+U")

        self.btnBrowse.clicked.connect(self.openFile)
        self.actionOpen.triggered.connect(self.openFile)
        self.actionExit.triggered.connect(self.closeApp)

    def openFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', "", "All files (*);;CSV Files (*.csv)")
        filePath = fname[0]
        self.lineEdit.setText(filePath)

    def closeApp(self):
        sys.exit()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())