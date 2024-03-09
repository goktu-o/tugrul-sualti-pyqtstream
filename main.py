from PyQt5 import QtWidgets, QtGui
from ui_main_window import Ui_MainWindow
import sys
import os
from datetime import datetime

class ImageCaptureApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect the clicked signal of the screenshotButton to the record_image method
        self.ui.screenshotButton.clicked.connect(self.record_image)

        # Set the window icon
        window_logo_path = "assets/tugrul-logo_16x16px.png"
        self.setWindowIcon(QtGui.QIcon(window_logo_path))  # Adjust the path according to your logo file

        # Add another tab for vehicle status
        self.ui.tabWidget.addTab(QtWidgets.QWidget(), "Araç Durumu")
        self.setup_vehicle_status_tab()

    def setup_vehicle_status_tab(self):
        # Add widgets for vehicle status tab
        # Example:
        # label_status = QtWidgets.QLabel("Vehicle Status")
        # label_sensor_value = QtWidgets.QLabel("Sensor Value: ")
        # self.ui.tabWidget.widget(1).layout().addWidget(label_status)
        #self.ui.tabWidget.widget(1).layout().addWidget(label_sensor_value)
        pass
    
    def record_image(self):
        # Capture the current frame from the label and save it
        pixmap = self.ui.label.pixmap()
        if pixmap is not None:
            # Get the current date and time
            current_time = datetime.now().strftime("%m_%d_%Y_%H%M%S")

            # Get the path to the desktop
            desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

            # Create the screenshots folder if it doesn't exist
            screenshots_folder = os.path.join(desktop_path, "screenshots")
            os.makedirs(screenshots_folder, exist_ok=True)

            # Save the screenshot to the desktop screenshots folder
            filename = f"{current_time}_recorded_image.png"
            screenshot_path = os.path.join(screenshots_folder, filename)
            pixmap.toImage().save(screenshot_path)

            # Display a message indicating the image has been saved
            QtWidgets.QMessageBox.information(self, "Image Captured", f"Image captured as: {filename}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = ImageCaptureApp()
    MainWindow.show()
    sys.exit(app.exec_())
