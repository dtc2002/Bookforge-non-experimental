import argparse
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from literary_ai.gui import MainWindow

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Literary AI GUI')
    parser.add_argument('mode', nargs='?', default='edit',
                        help='Mode: edit (default) or view')
    args = parser.parse_args()

    app = QApplication(sys.argv)
    window = MainWindow()
    if args.mode == 'view':
        window.setWindowFlags(window.windowFlags() | Qt.FramelessWindowHint)
        window.setAttribute(Qt.WA_TranslucentBackground)
        window.setWindowTitle("Literary AI Viewer")
    window.show()
    sys.exit(app.exec())