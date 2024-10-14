
from typing import TYPE_CHECKING, Optional

from PyQt6.QtWidgets import (QVBoxLayout, QWidget, QTabWidget)

from electrum.i18n import _
from electrum.logging import Logger
from .market.offer_book_tab import OfferBookTab
from .market.offers_by_currency_tab import OffersByCurrencyTab
from .market.offers_by_payment_method_tab import OffersByPaymentMethodTab
from .market.trades_tab import TradesTab
from ..styles import ChildTabStyle

if TYPE_CHECKING:
    from electrum.gui.qt.main_window import ElectrumWindow

class MarketTab(QWidget, Logger):

    def __init__(self, window: 'ElectrumWindow', parent: Optional['QWidget'] = ...):
        QWidget.__init__(self, parent)
        Logger.__init__(self)

        self.window = window
        self.wallet = window.wallet
        self.config = window.config
        
        vbox = QVBoxLayout(self)
        self.tabs = tabs = QTabWidget(self)
        self.offer_book_tab = OfferBookTab(window, self)
        self.offers_by_currency_tab = OffersByCurrencyTab(window, self)
        self.offers_by_payment_method_tab = OffersByPaymentMethodTab(window, self)
        self.trades_tab = TradesTab(window, self)
        tabs.addTab(self.offer_book_tab, _('Offer Book'))
        tabs.addTab(self.offers_by_currency_tab, _('Offers By Currency'))
        tabs.addTab(self.offers_by_payment_method_tab, _('Offers By Payment Method'))
        tabs.addTab(self.trades_tab, _('Trades'))
        tabs.setStyleSheet(ChildTabStyle)
        vbox.addWidget(tabs)
        vbox.setContentsMargins(2, 2, 2, 2)

