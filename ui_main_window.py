from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Create a vertical layout for the central widget
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        # Create a tab widget to hold the content
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")

        # Add the tab widget to the layout
        self.verticalLayout.addWidget(self.tabWidget)

        # Create the main functionality tab
        self.tabMainFunctionality = QtWidgets.QWidget()
        self.tabMainFunctionality.setObjectName("tabMainFunctionality")
        self.tabWidget.addTab(self.tabMainFunctionality, "Video Akışı")

        # Set up UI elements for the main functionality tab
        self.label = QtWidgets.QLabel(self.tabMainFunctionality)
        self.label.setGeometry(QtCore.QRect(10, 150, 640, 480))
        self.label.setObjectName("label")

        self.screenshotButton = QtWidgets.QPushButton(self.tabMainFunctionality)
        self.screenshotButton.setGeometry(QtCore.QRect(650, 30, 120, 40))
        self.screenshotButton.setObjectName("screenshotButton")
        self.screenshotButton.setText("Ekran Görüntüsü Al")

        self.recordInfoLabel = QtWidgets.QLabel(self.tabMainFunctionality)
        self.recordInfoLabel.setGeometry(QtCore.QRect(150, 30, 350, 40))
        self.recordInfoLabel.setObjectName("recordInfoLabel")

        self.imageLabel = QtWidgets.QLabel(self.tabMainFunctionality)
        self.imageLabel.setGeometry(QtCore.QRect(650, 10, 120, 20))
        self.imageLabel.setObjectName("imageLabel")
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imageLabel.setText("Resim")

        self.startRecordingButton = QtWidgets.QPushButton(self.tabMainFunctionality)
        self.startRecordingButton.setGeometry(QtCore.QRect(650, 130, 120, 40))
        self.startRecordingButton.setObjectName("startRecordingButton")
        self.startRecordingButton.setText("Kaydı durdur")

        self.stopRecordingButton = QtWidgets.QPushButton(self.tabMainFunctionality)
        self.stopRecordingButton.setGeometry(QtCore.QRect(650, 180, 120, 40))
        self.stopRecordingButton.setObjectName("stopRecordingButton")
        self.stopRecordingButton.setText("Kaydı Başlat")

        self.videoLabel = QtWidgets.QLabel(self.tabMainFunctionality)
        self.videoLabel.setGeometry(QtCore.QRect(650, 110, 120, 20))
        self.videoLabel.setObjectName("videoLabel")
        self.videoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.videoLabel.setText("Video")

        self.logoLabel = QtWidgets.QLabel(self.tabMainFunctionality)
        self.logoLabel.setGeometry(QtCore.QRect(10, 10, 100, 135))
        self.logoLabel.setObjectName("logoLabel")

        # Set the pixmap of the logoLabel to your logo image
        logo_path = "assets/tugrul-logo4_100x135px.png"
        self.logoLabel.setPixmap(QtGui.QPixmap(logo_path))

        # Add the central widget to the main window
        MainWindow.setCentralWidget(self.centralwidget)

        # Translate UI elements
        self.retranslateUi(MainWindow)

        # Connect slots by name
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tuğrul Su Altı Takımı - Yer Üstü İstasyonu"))
