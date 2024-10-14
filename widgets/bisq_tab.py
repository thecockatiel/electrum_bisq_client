
from typing import TYPE_CHECKING

from PyQt6.QtWidgets import (QVBoxLayout, QWidget, QTabWidget)

from electrum.i18n import _
from electrum.logging import Logger
from .tabs.market_tab import MarketTab
from .styles import MainTabsStyle

if TYPE_CHECKING:
    from electrum.gui.qt.main_window import ElectrumWindow

class BisqTab(QWidget, Logger):

    def __init__(self, window: 'ElectrumWindow'):
        QWidget.__init__(self, window)
        Logger.__init__(self)

        self.window = window
        self.wallet = window.wallet
        self.config = window.config
        
        vbox = QVBoxLayout(self)
        self.tabs = tabs = QTabWidget(self)
        self.market_tab = MarketTab(window, self) 
        tabs.setStyleSheet(MainTabsStyle)
        tabs.addTab(self.market_tab, _('Market'))
        vbox.addWidget(tabs)
        vbox.setContentsMargins(2, 2, 2, 2)

