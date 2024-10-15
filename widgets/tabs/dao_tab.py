
from typing import TYPE_CHECKING, Optional

from PyQt6.QtWidgets import (QVBoxLayout, QWidget, QTabWidget)

from electrum.i18n import _
from electrum.logging import Logger
from ..styles import ChildTabStyle

from .dao.facts_and_figures_tab import FactsAndFiguresTab
from .dao.bsq_wallet_tab import BsqWalletTab
from .dao.governance_tab import GovernanceTab
from .dao.bonding_tab import BondingTab
from .dao.proof_of_burn_tab import ProofOfBurnTab
from .dao.network_monitor_tab import NetworkMonitorTab

if TYPE_CHECKING:
    from electrum.gui.qt.main_window import ElectrumWindow

class DaoTab(QWidget, Logger):

    def __init__(self, window: 'ElectrumWindow', parent: Optional['QWidget'] = ...):
        QWidget.__init__(self, parent)
        Logger.__init__(self)

        self.window = window
        self.wallet = window.wallet
        self.config = window.config
        
        vbox = QVBoxLayout(self)
        self.tabs = tabs = QTabWidget(self)
        self.facts_and_figures_tab = FactsAndFiguresTab(window, self)
        self.bsq_wallet_tab = BsqWalletTab(window, self)
        self.governance_tab = GovernanceTab(window, self)
        self.bonding_tab = BondingTab(window, self)
        self.proof_of_burn_tab = ProofOfBurnTab(window, self)
        self.network_monitor_tab = NetworkMonitorTab(window, self)
        tabs.addTab(self.facts_and_figures_tab, _('Facts & Figures'))
        tabs.addTab(self.bsq_wallet_tab, _('BSQ Wallet'))
        tabs.addTab(self.governance_tab, _('Governance'))
        tabs.addTab(self.bonding_tab, _('Bonding'))
        tabs.addTab(self.proof_of_burn_tab, _('Proof of Burn'))
        tabs.addTab(self.network_monitor_tab, _('Network Monitor'))
        tabs.setStyleSheet(ChildTabStyle)
        vbox.addWidget(tabs)
        vbox.setContentsMargins(2, 2, 2, 2)

