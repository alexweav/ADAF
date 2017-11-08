"""
Plugin Base Class

"""
class PluginBase:

    pluginEngine = 0

    def __init__(self, pluginEngine):
        self.pluginEngine = pluginEngine

    def run(self):
        return
