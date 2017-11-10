"""
Plugin Base Class
"""
class PluginBase:
    pluginEngine = 0

    """
    Init will store a reference to the pluginEngine
    """
    def __init__(self, pluginEngine):
        self.pluginEngine = pluginEngine
