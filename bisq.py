from electrum.plugin import BasePlugin, hook

class BisqPlugin(BasePlugin):

    def __init__(self, parent, config, name):
        BasePlugin.__init__(self, parent, config, name)
        