from video_server import VideoServer
from PyQt5 import QtWidgets
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = VideoServer()
    sys.exit(app.exec_())
