import sys
from pathlib import Path
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QFile, QIODevice, QDir
from PySide6.QtUiTools import QUiLoader
from animated_toggle import AnimatedToggle


class MainWindow(QMainWindow):
    def __init__(self, ui_path, parent=None):
        super().__init__(parent)
        self.ui = None
        self.setWindowTitle("TicTac-Dashboard")
        self.setGeometry(100, 100, 800, 450) 
        self._load_ui(ui_path)
        self.showMaximized()

    def _load_ui(self, ui_path):
        ui_file = QFile(str(ui_path))
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open {ui_path}: {ui_file.errorString()}")
            sys.exit(-1)

        loader = QUiLoader()
        loader.registerCustomWidget(AnimatedToggle)
        loader.setWorkingDirectory(QDir(str(Path(ui_path).parent)))
        self.ui = loader.load(ui_file)
        ui_file.close()

        if not self.ui:
            print(loader.errorString())
            sys.exit(-1)

        self.setCentralWidget(self.ui)

    def __getattr__(self, name):
        ui = self.__dict__.get("ui")
        if ui is None:
            raise AttributeError(name)
        return getattr(ui, name)
    