import cv2
import os
import socket
import numpy
import pickle
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage
from PyQt5.QtCore import QTimer
from datetime import datetime
from ui_main_window import Ui_MainWindow

class VideoServer(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.ip = "169.254.112.175"  # Your server IP
        self.port = 6666
        self.s.bind((self.ip, self.port))

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        # Connect the clicked signal of the recordButton to the record_image method
        self.ui.recordButton.clicked.connect(self.record_image)

        # Create a timer to clear the recording information after a certain time
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.clear_record_info)
        
        # Start receiving frames
        self.receive_frames()

    def receive_frames(self):
        while True:
            x = self.s.recvfrom(1000000)
            clientip = x[1][0]
            data = x[0]

            data = pickle.loads(data)
            data = cv2.imdecode(data, cv2.IMREAD_COLOR)

            # Display the received frame
            self.update_frame(data)

            if cv2.waitKey(10) == 27:
                break

    def update_frame(self, frame):
        # Convert the frame to QImage and display it in the UI
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.ui.label.setPixmap(QtGui.QPixmap.fromImage(image))

    def record_image(self):
        # Capture the current frame from the label and save it
        pixmap = self.ui.label.pixmap()
        if pixmap is not None:
            # Get the current date and time
            current_time = datetime.now().strftime("%m%d%Y_%H%M%S")
            filename = f"{current_time}_recorded_image.png"

            # Check if the file already exists
            counter = 1
            while os.path.exists(filename):
                # If the file exists, append a counter to make the filename unique
                filename = f"{current_time}_recorded_image_{counter}.png"
                counter += 1

            pixmap.toImage().save(filename)
            self.ui.recordInfoLabel.setText(f"Image recorded as: {filename}")
            self.timer.start(2000)  # Clear the message after 2 seconds
    
    def clear_record_info(self):
        self.ui.recordInfoLabel.clear()
