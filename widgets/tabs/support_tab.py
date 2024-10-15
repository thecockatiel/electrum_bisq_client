
from typing import TYPE_CHECKING, Optional

from PyQt6.QtWidgets import (QVBoxLayout, QWidget, QTabWidget)

from electrum.i18n import _
from electrum.logging import Logger
from ..styles import ChildTabStyle

from .support.mediation_tab import MediationTab
from .support.arbitration_tab import ArbitrationTab 

if TYPE_CHECKING:
    from electrum.gui.qt.main_window import ElectrumWindow

class SupportTab(QWidget, Logger):

    def __init__(self, window: 'ElectrumWindow', parent: Optional['QWidget'] = ...):
        QWidget.__init__(self, parent)
        Logger.__init__(self)

        self.window = window
        self.wallet = window.wallet
        self.config = window.config
        
        vbox = QVBoxLayout(self)
        self.tabs = tabs = QTabWidget(self)
        self.mediation_tab = MediationTab(window, self)
        self.arbitration_tab = ArbitrationTab(window, self)
        tabs.addTab(self.mediation_tab, _('Mediation'))
        tabs.addTab(self.arbitration_tab, _('Arbitration'))
        tabs.setStyleSheet(ChildTabStyle)
        vbox.addWidget(tabs)
        vbox.setContentsMargins(2, 2, 2, 2)

