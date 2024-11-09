from typing import TYPE_CHECKING

from electrum.plugin import BasePlugin, hook
from pathlib import Path
import os
from functools import lru_cache
from PyQt6.QtGui import (QIcon)

if TYPE_CHECKING:
    from electrum.gui.qt import ElectrumGui

# absolute path to python package folder of electrum ("lib")
plugin_dir = os.path.split(os.path.realpath(__file__))[0]

def resource_path(*parts):
    return os.path.join(plugin_dir, "resources", *parts)

@lru_cache(maxsize=1000)
def read_QIcon(icon_basename: str) -> QIcon:
    return QIcon(resource_path(icon_basename))

class BisqPlugin(BasePlugin):

    def __init__(self, parent, config, name):
        BasePlugin.__init__(self, parent, config, name)
