
from typing import TYPE_CHECKING

from PyQt6.QtWidgets import (QVBoxLayout, QWidget, QTabWidget)

from electrum.i18n import _
from electrum.logging import Logger
from .tabs.market_tab import MarketTab
from .tabs.buy_tab import BuyTab
from .tabs.sell_tab import SellTab
from .tabs.portfolio_tab import PortfolioTab
from .tabs.funds_tab import FundsTab
from .tabs.support_tab import SupportTab
from .tabs.settings_tab import SettingsTab
from .tabs.account_tab import AccountTab
from .tabs.dao_tab import DaoTab
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
        self.buy_tab = BuyTab(window, self) 
        self.sell_tab = SellTab(window, self) 
        self.portfolio_tab = PortfolioTab(window, self) 
        self.funds_tab = FundsTab(window, self) 
        self.support_tab = SupportTab(window, self) 
        self.settings_tab = SettingsTab(window, self) 
        self.account_tab = AccountTab(window, self) 
        self.dao_tab = DaoTab(window, self) 
        tabs.setStyleSheet(MainTabsStyle)
        tabs.addTab(self.market_tab, _('Market'))
        tabs.addTab(self.buy_tab, _('Buy'))
        tabs.addTab(self.sell_tab, _('Sell'))
        tabs.addTab(self.portfolio_tab, _('Portfolio'))
        tabs.addTab(self.funds_tab, _('Funds'))
        tabs.addTab(self.support_tab, _('Support'))
        tabs.addTab(self.settings_tab, _('Settings'))
        tabs.addTab(self.account_tab, _('Account'))
        tabs.addTab(self.dao_tab, _('DAO'))
        vbox.addWidget(tabs)
        vbox.setContentsMargins(2, 2, 2, 2)

