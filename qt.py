from typing import TYPE_CHECKING

from electrum.plugin import hook
from .bisq import BisqPlugin
from .widgets.bisq_tab import BisqTab
import os
from functools import lru_cache
from PyQt6.QtGui import (QIcon)

if TYPE_CHECKING:
    from electrum.gui.qt import ElectrumGui
    from electrum.gui.qt.main_window import ElectrumWindow
    from electrum.wallet import Abstract_Wallet
    
def resource_path(*parts):
    return os.path.join(plugin_dir, "resources", *parts)

@lru_cache(maxsize=1000)
def read_QIcon(icon_basename: str) -> QIcon:
    return QIcon(resource_path(icon_basename))

# absolute path to python package folder of electrum ("lib")
plugin_dir = os.path.split(os.path.realpath(__file__))[0]

class Plugin(BisqPlugin):

    def __init__(self, parent, config, name):
        super().__init__(parent, config, name)
        self._init_qt_received = False
        
    @hook
    def init_qt(self, gui: 'ElectrumGui'):
        if self._init_qt_received:  # only need/want the first signal
            return
        self._init_qt_received = True
        # If the user just enabled the plugin, the 'load_wallet' hook would not
        # get called for already loaded wallets, hence we call it manually for those:
        for window in gui.windows:
            self.load_wallet(window.wallet, window)

    @hook
    def load_wallet(self, wallet: 'Abstract_Wallet', window: 'ElectrumWindow'):
        window.bisq_tab = BisqTab(window)
        window.tabs.insertTab(0, window.bisq_tab, read_QIcon("bisq.png"), 'bisq')
        window.tabs.setCurrentIndex(0)