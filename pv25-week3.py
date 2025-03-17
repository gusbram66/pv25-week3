import sys
import random
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtCore import Qt

class MouseTracker(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mouse Tracker")
        self.setGeometry(100, 100, 600, 400)
        self.setMouseTracking(True)  

        self.label = QLabel("Move the mouse!", self)
        self.label.move(250, 180)  

    def mouseMoveEvent(self, event):
        self.label.setText(f"Mouse: {event.x()}, {event.y()}")

    def enterEvent(self, event):
        self.setMouseTracking(True)

    def leaveEvent(self, event):
        self.setMouseTracking(False)

    def eventFilter(self, obj, event):
        if obj == self.label and event.type() == event.Enter:
            new_x = random.randint(0, self.width() - self.label.width())
            new_y = random.randint(0, self.height() - self.label.height())
            self.label.move(new_x, new_y)
        return super().eventFilter(obj, event)

    def showEvent(self, event):
        self.label.installEventFilter(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MouseTracker()
    window.show()
    sys.exit(app.exec_())
