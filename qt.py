from typing import TYPE_CHECKING

from electrum.plugin import hook
from .bisq_plugin import BisqPlugin, read_QIcon
from .widgets.bisq_tab import BisqTab

if TYPE_CHECKING:
    from electrum.gui.qt import ElectrumGui
    from electrum.gui.qt.main_window import ElectrumWindow
    from electrum.wallet import Abstract_Wallet

class Plugin(BisqPlugin):

    def __init__(self, parent, config, name):
        super().__init__(parent, config, name)
        self._init_qt_received = False
        
    @hook
    def init_qt(self, gui: 'ElectrumGui'):
        super().init_qt(gui)
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