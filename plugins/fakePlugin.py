from sys import path
from os.path import dirname as dir
path.append(dir(path[0]))
from PluginSystem import PluginBase

"""
Plugin used for testing.

The class name must be the same as the file name.
"""
class FakePlugin(PluginBase.PluginBase):

    def init(self):
        self.pluginEngine.RegisterCallback("realtime", "HelloWorld", ["cameraStills"])

    def HelloWorld(self, cameraStills):
        print(cameraStills)
