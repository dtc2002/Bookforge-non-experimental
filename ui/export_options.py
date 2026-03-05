from PySide6.QtWidgets import (QApplication, QMainWindow, QComboBox, QPushButton,
    QLabel, QWidget, QHBoxLayout)
from PySide6.QtCore import Qt

class ExportOptions(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Export Options")
        self.setGeometry(100, 100, 300, 150)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.format_label = QLabel("Export Format:")
        self.layout.addWidget(self.format_label)

        self.format_combo = QComboBox()
        self.format_combo.addItem("Markdown")
        self.format_combo.addItem("DOCX")
        self.layout.addWidget(self.format_combo)

        self.export_button = QPushButton("Export")
        self.export_button.clicked.connect(self.export_document)
        self.layout.addWidget(self.export_button)

    def export_document(self):
        format = self.format_combo.currentText()
        # Implement export logic based on selected format
        pass

if __name__ == "__main__":
    app = QApplication([])
    window = ExportOptions()
    window.show()
    app.exec()