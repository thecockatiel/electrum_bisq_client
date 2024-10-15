from typing import TYPE_CHECKING, Optional

from PyQt6.QtWidgets import (QVBoxLayout, QWidget, QLabel)

from electrum.i18n import _
from electrum.logging import Logger

if TYPE_CHECKING:
    from electrum.gui.qt.main_window import ElectrumWindow

class OpenTradesTab(QWidget, Logger):

    def __init__(self, window: 'ElectrumWindow', parent: Optional['QWidget'] = ...):
        QWidget.__init__(self, parent)
        Logger.__init__(self)

        self.window = window
        self.wallet = window.wallet
        self.config = window.config
        
        vbox = QVBoxLayout(self)
        vbox.addWidget(QLabel(_("Test")))
        vbox.addStretch()

