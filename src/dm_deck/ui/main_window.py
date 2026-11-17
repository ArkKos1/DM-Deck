from pathlib import Path

from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (
  QMainWindow,
  QPushButton,
  QToolButton,
  QLabel,
  QTabWidget,
  QWidget,
  QFrame,
  QStackedWidget
)

from src.dm_deck.ui.preset_widget import SoundboardWidget

UI_DIR = Path(__file__).resolve().parents[3] / "ui"


class MainWindow(QMainWindow):
  def __init__(self,parent=None):
    super().__init__(parent)
    loader = QUiLoader()
    file = QFile(str(UI_DIR / "main_window.ui"))
    self.window = loader.load(file)
    file.close()
    # self._init_state()
    self._find_widgets()
    self._init_pages()
    self._signal_connect()
    self.window.show()

  def _find_widgets(self):
    # MENU BUTTONS
    self.soundboard_button = self._find(QPushButton, "soundboardPushButton")
    self.music_library_button = self._find(QPushButton, "musicLibraryPushButton")
    self.settings_button = self._find(QPushButton, "settingsPushButton")
    self.about_button = self._find(QPushButton, "aboutPushButton")

    #STACKED WIDGET
    self.central_region = self._find(QStackedWidget, "centralStackedWidget")

  def _init_pages(self):
    self.soundboard_page = SoundboardWidget()

    self.central_region.addWidget(self.soundboard_page)

  def _signal_connect(self):
    # MENU BUTTONS
    self.soundboard_button.clicked.connect(lambda: self._stacked_widget("soundboard"))

# HELPING FUNCTIONS
  def _find(self,cls,name):
    widget = self.window.findChild(cls,name)
    if widget is None:
      print(f"Couldn't load widget {cls}:{name}")
    else:
      return widget
    
  def _stacked_widget(self,name):
    INDEX_OF_PAGE = {
    "soundboard": self.soundboard_page 
    }
    widget = INDEX_OF_PAGE.get(name)
    current_widget = self.central_region.currentWidget()
    if widget is not None and widget != current_widget:
      self.central_region.setCurrentWidget(widget)
      print("I did")

    # index = INDEX_OF_PAGE.get(name)
    # current_index = self.central_region.currentIndex()
    # if index is not None and index != current_index:
    #   self.central_region.setCurrentIndex(index)

    

    
