from PySide6.QtWidgets import (QApplication, QMainWindow, QListWidget, QListWidgetItem,
    QSlider, QVBoxLayout, QWidget, QPushButton, QLabel, QHBoxLayout)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction

class SceneItem(QListWidgetItem):
    def __init__(self, text, pacing=1.0):
        super().__init__(text)
        self.pacing = pacing

class SceneSliderDelegate(QListWidget):
    def __init__(self):
        super().__init__()
        self.setDragDropMode(QListWidget.DragDrop)
        self.setDefaultDropAction(Qt.MoveAction)
        self.setStyleSheet("background-color: #f0f0f0;")

    def add_scene(self, text, pacing=1.0):
        item = SceneItem(text, pacing)
        self.addItem(item)
        self.scrollToBottom()

    def get_scenes(self):
        return [self.item(i) for i in range(self.count())]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Literary AI Editor")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.scene_list = SceneSliderDelegate()
        self.layout.addWidget(self.scene_list)

        self.add_button = QPushButton("Add Scene")
        self.add_button.clicked.connect(self.add_scene)
        self.layout.addWidget(self.add_button)

    def add_scene(self):
        scene = QListWidgetItem("New Scene")
        self.scene_list.addItem(scene)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()