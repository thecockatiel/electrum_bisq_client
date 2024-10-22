from typing import TYPE_CHECKING

from electrum.plugin import BasePlugin, hook
from pathlib import Path
import os
from functools import lru_cache
from PyQt6.QtGui import (QIcon)

if TYPE_CHECKING:
    from electrum.gui.qt import ElectrumGui

from .tor import TorManager

# absolute path to python package folder of electrum ("lib")
plugin_dir = os.path.split(os.path.realpath(__file__))[0]

def resource_path(*parts):
    return os.path.join(plugin_dir, "resources", *parts)

@lru_cache(maxsize=1000)
def read_QIcon(icon_basename: str) -> QIcon:
    return QIcon(resource_path(icon_basename))

def read_resource_lines(resource_name: str) -> str:
    try:
        with open(resource_path(resource_name), 'r') as f:
            return f.readlines()
    except FileNotFoundError:
            return None

class BisqPlugin(BasePlugin):

    def __init__(self, parent, config, name):
        BasePlugin.__init__(self, parent, config, name)
        self._stopped = True
        self.gui = None
        self.root_dir = Path(self.config.electrum_path_root()).joinpath("bisq")
        self.root_dir.mkdir(parents=True, exist_ok=True)

        self.tor_manager = TorManager(self.root_dir)
        self.tor_manager.proxy_port.connect(self.onTorSetupFinished)
        self.tor_manager.having_trouble.connect(self.onTorFailed)
        
    @hook
    def init_qt(self, gui: 'ElectrumGui'):
        self.gui = gui
        if (self._stopped):
            self._stopped = False
            self.tor_manager.setup_tor()

    @hook
    def on_close_window(self, window):
        # stop bisq on last window closed
        if not self.gui or not self.gui.windows:
            self._stopped = True
            # todo: drop peer connections

    def onTorSetupFinished(self, socks_port: str):
        print('Tor running at: ' + socks_port)

    def onTorFailed(self):
        print('Tor setup failed')