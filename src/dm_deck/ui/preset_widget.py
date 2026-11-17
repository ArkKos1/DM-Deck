from pathlib import Path

from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (
  QWidget,
  QVBoxLayout,
  QPushButton
)

UI_DIR = Path(__file__).resolve().parents[3] / "ui"

class SoundboardWidget(QWidget):
  def __init__(self,parent=None):
    super().__init__(parent)
    loader = QUiLoader()
    ui_file = QFile(str(UI_DIR / "preset_widget.ui"))
    self.widget = loader.load(ui_file)
    ui_file.close()

    layout = QVBoxLayout(self)
    layout.setContentsMargins(0, 0, 0, 0)
    layout.addWidget(self.widget)


    