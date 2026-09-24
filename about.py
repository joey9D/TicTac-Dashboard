from pathlib import Path
from PySide6.QtCore import QFile, QIODevice, QDir
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QDialog, QVBoxLayout

import globals as g


class About(QDialog):

    _instance = None  # hält das eine offene Info-Fenster

    def __init__(self, ui_path, parent=None):
        super().__init__(parent)
        self.ui = None
        self.setWindowTitle("Dashboard-Version")
        # self.setGeometry(100, 100, 400, 225)
        self.resize(400, 225)
        self._load_ui(ui_path)

    def _load_ui(self, ui_path):
        ui_file = QFile(str(ui_path))
        if not ui_file.open(QIODevice.ReadOnly):
            raise FileNotFoundError(f"Cannot open {g.UI_ABOUT}: {ui_file.errorString()}")

        loader = QUiLoader()
        loader.setWorkingDirectory(QDir(str(Path(ui_path).parent)))
        self.ui = loader.load(ui_file, self)
        ui_file.close()

        if self.ui is None:
            raise RuntimeError(loader.errorString())

        # Geladenen Inhalt in diesen Dialog einbetten
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.ui)

        # Falls about.ui als "Dialog with Buttons" angelegt wurde
        if hasattr(self.ui, "buttonBox"):
            self.ui.buttonBox.accepted.connect(self.accept)
            self.ui.buttonBox.rejected.connect(self.reject)

        if hasattr(self.ui, "lbl_Version"):
            self.ui.lbl_Version.setText(f"Version {g.APP_VERSION}")

    @classmethod
    def show_about(cls, ui_path, parent=None):
        print("show_about aufgerufen")
        if cls._instance is None:
            cls._instance = cls(ui_path, parent)
            cls._instance.finished.connect(cls._on_closed)

        cls._instance.show()
        cls._instance.raise_()
        cls._instance.activateWindow()

    @classmethod
    def _on_closed(cls):
        cls._instance = None