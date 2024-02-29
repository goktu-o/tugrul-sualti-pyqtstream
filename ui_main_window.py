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
        self.screenshotButton = QtWidgets.QPushButton(self.centralwidget)
        self.screenshotButton.setGeometry(QtCore.QRect(670, 30, 120, 40))
        self.screenshotButton.setObjectName("screenshotButton")
        self.screenshotButton.setText("Capture")
        self.recordInfoLabel = QtWidgets.QLabel(self.centralwidget)
        self.recordInfoLabel.setGeometry(QtCore.QRect(150, 30, 350, 40))
        self.recordInfoLabel.setObjectName("recordInfoLabel")

        # Add QLabel for 'image' label
        self.imageLabel = QtWidgets.QLabel(self.centralwidget)
        self.imageLabel.setGeometry(QtCore.QRect(670, 10, 120, 20))
        self.imageLabel.setObjectName("imageLabel")
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imageLabel.setText("Image")

        # Add buttons for video recording
        self.startRecordingButton = QtWidgets.QPushButton(self.centralwidget)
        self.startRecordingButton.setGeometry(QtCore.QRect(670, 130, 120, 40))
        self.startRecordingButton.setObjectName("startRecordingButton")
        self.startRecordingButton.setText("Start Recording")

        self.stopRecordingButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopRecordingButton.setGeometry(QtCore.QRect(670, 180, 120, 40))
        self.stopRecordingButton.setObjectName("stopRecordingButton")
        self.stopRecordingButton.setText("Stop Recording")

        # Add QLabel for 'video' label
        self.videoLabel = QtWidgets.QLabel(self.centralwidget)
        self.videoLabel.setGeometry(QtCore.QRect(670, 110, 120, 20))
        self.videoLabel.setObjectName("videoLabel")
        self.videoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.videoLabel.setText("Video")

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