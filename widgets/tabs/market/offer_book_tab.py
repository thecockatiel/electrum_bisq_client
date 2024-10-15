
from typing import TYPE_CHECKING, Optional

from PyQt6.QtWidgets import (QVBoxLayout, QWidget, QLabel)

from electrum.i18n import _
from electrum.logging import Logger

from ...charts.offer_book_chart import OfferBookChart

if TYPE_CHECKING:
    from electrum.gui.qt.main_window import ElectrumWindow

class OfferBookTab(QWidget, Logger):

    def __init__(self, window: 'ElectrumWindow', parent: Optional['QWidget'] = ...):
        QWidget.__init__(self, parent)
        Logger.__init__(self)

        self.window = window
        self.wallet = window.wallet
        self.config = window.config
        
        vbox = QVBoxLayout(self)
        self.offer_book_chart = OfferBookChart(self)
        vbox.addWidget(self.offer_book_chart)
        vbox.addStretch()

