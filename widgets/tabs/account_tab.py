
from typing import TYPE_CHECKING, Optional

from PyQt6.QtWidgets import (QVBoxLayout, QWidget, QTabWidget)

from electrum.i18n import _
from electrum.logging import Logger
from ..styles import ChildTabStyle

from .account.national_currency_accounts_tab import NationalCurrencyAccountsTab
from .account.altcoin_accounts_tab import AltcoinAccountsTab
from .account.notifications_tab import NotificationsTab

if TYPE_CHECKING:
    from electrum.gui.qt.main_window import ElectrumWindow

class AccountTab(QWidget, Logger):

    def __init__(self, window: 'ElectrumWindow', parent: Optional['QWidget'] = ...):
        QWidget.__init__(self, parent)
        Logger.__init__(self)

        self.window = window
        self.wallet = window.wallet
        self.config = window.config
        
        vbox = QVBoxLayout(self)
        self.tabs = tabs = QTabWidget(self)
        self.national_currency_accounts_tab = NationalCurrencyAccountsTab(window, self)
        self.altcoin_accounts_tab = AltcoinAccountsTab(window, self)
        self.notifications_tab = NotificationsTab(window, self)
        tabs.addTab(self.national_currency_accounts_tab, _('National Currency Accounts'))
        tabs.addTab(self.altcoin_accounts_tab, _('Altcoin Accounts'))
        tabs.addTab(self.notifications_tab, _('Notifications'))
        tabs.setStyleSheet(ChildTabStyle)
        vbox.addWidget(tabs)
        vbox.setContentsMargins(2, 2, 2, 2)

