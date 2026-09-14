import sys
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtUiTools import QUiLoader
from animated_toggle import AnimatedToggle


class MainWindow(QMainWindow):
    def __init__(self, ui_file, parent=None):
        super().__init__(parent)
        self._load_ui(ui_file)
        # self._connect_signales()
        
    def _load_ui(self, ui_file):
        ui_file = QFile(ui_file)
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open {ui_file}: {ui_file.errorString()}")
            sys.exit(-1)
        
        loader = QUiLoader()
        loader.registerCustomWidget(AnimatedToggle)
        
        ui_content = loader.load(ui_file, self)
        ui_file.close()
        
        if not ui_content:
            print(loader.errorString())
            sys.exit(-1)
            
