
from typing import TYPE_CHECKING, Optional

from PyQt6.QtWidgets import (QVBoxLayout, QWidget, QTabWidget)

from electrum.i18n import _
from electrum.logging import Logger
from ..styles import ChildTabStyle

from .funds.reserved_funds_tab import ReservedFundsTab
from .funds.locked_funds_tab import LockedFundsTab
from .funds.transactions_tab import TransactionsTab

if TYPE_CHECKING:
    from electrum.gui.qt.main_window import ElectrumWindow

class FundsTab(QWidget, Logger):

    def __init__(self, window: 'ElectrumWindow', parent: Optional['QWidget'] = ...):
        QWidget.__init__(self, parent)
        Logger.__init__(self)

        self.window = window
        self.wallet = window.wallet
        self.config = window.config
        
        vbox = QVBoxLayout(self)
        self.tabs = tabs = QTabWidget(self)
        self.reserved_funds_tab = ReservedFundsTab(window, self)
        self.locked_funds_tab = LockedFundsTab(window, self)
        self.transactions_tab = TransactionsTab(window, self)
        tabs.addTab(self.reserved_funds_tab, _('Reserved Funds'))
        tabs.addTab(self.locked_funds_tab, _('Locked Funds'))
        tabs.addTab(self.transactions_tab, _('Transactions'))
        tabs.setStyleSheet(ChildTabStyle)
        vbox.addWidget(tabs)
        vbox.setContentsMargins(2, 2, 2, 2)

