
from typing import TYPE_CHECKING, Optional

from PyQt6.QtWidgets import (QVBoxLayout, QWidget, QTabWidget)

from electrum.i18n import _
from electrum.logging import Logger
from ..styles import ChildTabStyle

from .settings.preferences_tab import PreferencesTab
from .settings.network_info_tab import NetworkInfoTab
from .settings.about_tab import AboutTab

if TYPE_CHECKING:
    from electrum.gui.qt.main_window import ElectrumWindow

class SettingsTab(QWidget, Logger):

    def __init__(self, window: 'ElectrumWindow', parent: Optional['QWidget'] = ...):
        QWidget.__init__(self, parent)
        Logger.__init__(self)

        self.window = window
        self.wallet = window.wallet
        self.config = window.config
        
        vbox = QVBoxLayout(self)
        self.tabs = tabs = QTabWidget(self)
        self.preferences_tab = PreferencesTab(window, self)
        self.network_info_tab = NetworkInfoTab(window, self)
        self.about_tab = AboutTab(window, self)
        tabs.addTab(self.preferences_tab, _('Preferences'))
        tabs.addTab(self.network_info_tab, _('Network Info'))
        tabs.addTab(self.about_tab, _('About')) 
        tabs.setStyleSheet(ChildTabStyle)
        vbox.addWidget(tabs)
        vbox.setContentsMargins(2, 2, 2, 2)

