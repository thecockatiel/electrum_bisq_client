
from typing import TYPE_CHECKING, Optional

from PyQt6.QtWidgets import (QVBoxLayout, QWidget, QTabWidget)

from electrum.i18n import _
from electrum.logging import Logger
from .sell.sell_bitcoin_tab import SellBitcoinTab
from .sell.sell_bsq_tab import SellBsqTab
from .sell.sell_xmr_tab import SellXmrTab
from .sell.sell_other_tab import SellOtherTab
from ..styles import ChildTabStyle

if TYPE_CHECKING:
    from electrum.gui.qt.main_window import ElectrumWindow

class SellTab(QWidget, Logger):

    def __init__(self, window: 'ElectrumWindow', parent: Optional['QWidget'] = ...):
        QWidget.__init__(self, parent)
        Logger.__init__(self)

        self.window = window
        self.wallet = window.wallet
        self.config = window.config
        
        vbox = QVBoxLayout(self)
        self.tabs = tabs = QTabWidget(self)
        self.sell_bitcoin_tab = SellBitcoinTab(window, self)
        self.sell_bsq_tab = SellBsqTab(window, self)
        self.sell_xmr_tab = SellXmrTab(window, self)
        self.sell_other_tab = SellOtherTab(window, self)
        tabs.addTab(self.sell_bitcoin_tab, _('Bitcoin'))
        tabs.addTab(self.sell_bsq_tab, _('BSQ'))
        tabs.addTab(self.sell_xmr_tab, _('XMR'))
        tabs.addTab(self.sell_other_tab, _('Other'))
        tabs.setStyleSheet(ChildTabStyle)
        vbox.addWidget(tabs)
        vbox.setContentsMargins(2, 2, 2, 2)

