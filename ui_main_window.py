from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 150, 640, 480))
        self.label.setObjectName("label")        
        self.recordButton = QtWidgets.QPushButton(self.centralwidget)
        self.recordButton.setGeometry(QtCore.QRect(670, 30, 120, 40))
        self.recordButton.setObjectName("recordButton")
        self.recordButton.setText("Record")
        self.recordInfoLabel = QtWidgets.QLabel(self.centralwidget)
        self.recordInfoLabel.setGeometry(QtCore.QRect(150, 30, 350, 40))
        self.recordInfoLabel.setObjectName("recordInfoLabel")

        # Add a QLabel for your logo
        self.logoLabel = QtWidgets.QLabel(self.centralwidget)
        self.logoLabel.setGeometry(QtCore.QRect(10, 10, 100, 135))
        self.logoLabel.setObjectName("logoLabel")

        # Set the pixmap of the logoLabel to your logo image
        logo_path = "assets/tugrul-logo4_100x135px.png"
        self.logoLabel.setPixmap(QtGui.QPixmap(logo_path))

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Video Stream"))
