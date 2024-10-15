
from typing import TYPE_CHECKING, Optional

from PyQt6.QtWidgets import (QVBoxLayout, QWidget, QTabWidget)

from electrum.i18n import _
from electrum.logging import Logger
from .buy.buy_bitcoin_tab import BuyBitcoinTab
from .buy.buy_bsq_tab import BuyBsqTab
from .buy.buy_xmr_tab import BuyXmrTab
from .buy.buy_other_tab import BuyOtherTab
from ..styles import ChildTabStyle

if TYPE_CHECKING:
    from electrum.gui.qt.main_window import ElectrumWindow

class BuyTab(QWidget, Logger):

    def __init__(self, window: 'ElectrumWindow', parent: Optional['QWidget'] = ...):
        QWidget.__init__(self, parent)
        Logger.__init__(self)

        self.window = window
        self.wallet = window.wallet
        self.config = window.config
        
        vbox = QVBoxLayout(self)
        self.tabs = tabs = QTabWidget(self)
        self.buy_bitcoin_tab = BuyBitcoinTab(window, self)
        self.buy_bsq_tab = BuyBsqTab(window, self)
        self.buy_xmr_tab = BuyXmrTab(window, self)
        self.buy_other_tab = BuyOtherTab(window, self)
        tabs.addTab(self.buy_bitcoin_tab, _('Bitcoin'))
        tabs.addTab(self.buy_bsq_tab, _('BSQ'))
        tabs.addTab(self.buy_xmr_tab, _('XMR'))
        tabs.addTab(self.buy_other_tab, _('Other'))
        tabs.setStyleSheet(ChildTabStyle)
        vbox.addWidget(tabs)
        vbox.setContentsMargins(2, 2, 2, 2)

