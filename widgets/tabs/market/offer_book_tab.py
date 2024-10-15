
from typing import TYPE_CHECKING, Optional

from PyQt6.QtWidgets import (QVBoxLayout, QWidget, QLabel)

from electrum.i18n import _
from electrum.logging import Logger

from ...charts.offer_book_chart import OfferBookChart

import numpy as np

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
        
        sell_prices = np.array([53000, 53500, 55400, 55600, 55600, 60000, 63400])
        sell_volumes = np.array([0.51, 0.42, 0.39, 0.37, 0.36, 0.36, 0.25])

        buy_prices = np.array([65500, 65700, 66700, 68000, 69000, 70000, 70100, 70200, 71200])
        buy_volumes = np.array([0.08, 0.12, 0.25, 0.27, 0.35, 0.75, 0.75, 0.75, 1.00])
        
        self.offer_book_chart.updatePlot(sell_prices, sell_volumes, buy_prices, buy_volumes)


