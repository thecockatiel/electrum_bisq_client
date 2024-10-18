from .bisq_plugin import BisqPlugin

class BisqCmdLineHandler():

    def test(self):
        pass
    
class Plugin(BisqPlugin):
    handler = BisqCmdLineHandler()

    def create_handler(self, window):
        return self.handler
