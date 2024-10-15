
from typing import TYPE_CHECKING, Optional

from PyQt6.QtWidgets import (QVBoxLayout, QWidget, QTabWidget)

from electrum.i18n import _
from electrum.logging import Logger
from .portfolio.my_open_offers_tab import MyOpenOffersTab
from .portfolio.open_trades_tab import OpenTradesTab
from .portfolio.unconfirmed_bsq_swaps_tab import UnconfirmedBsqSwapsTab
from .portfolio.history_tab import HistoryTab
from ..styles import ChildTabStyle

if TYPE_CHECKING:
    from electrum.gui.qt.main_window import ElectrumWindow

class PortfolioTab(QWidget, Logger):

    def __init__(self, window: 'ElectrumWindow', parent: Optional['QWidget'] = ...):
        QWidget.__init__(self, parent)
        Logger.__init__(self)

        self.window = window
        self.wallet = window.wallet
        self.config = window.config
        
        vbox = QVBoxLayout(self)
        self.tabs = tabs = QTabWidget(self)
        self.my_open_offers_tab = MyOpenOffersTab(window, self)
        self.open_trades_tab = OpenTradesTab(window, self)
        self.unconfirmed_bsq_swaps_tab = UnconfirmedBsqSwapsTab(window, self)
        self.history_tab = HistoryTab(window, self)
        tabs.addTab(self.my_open_offers_tab, _('My Open Offers'))
        tabs.addTab(self.open_trades_tab, _('Open Trades'))
        tabs.addTab(self.unconfirmed_bsq_swaps_tab, _('Unconfirmed BSQ Swaps'))
        tabs.addTab(self.history_tab, _('History'))
        tabs.setStyleSheet(ChildTabStyle)
        vbox.addWidget(tabs)
        vbox.setContentsMargins(2, 2, 2, 2)

