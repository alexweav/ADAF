from sys import path
from os.path import dirname as dir
path.append(dir(path[0]))
from PluginSystem import PluginBase

"""
Plugin used for testing.

The class name must be the same as the file name. (Case Sensitive)
"""
class FakePlugin(PluginBase.PluginBase):

    def init(self):
        self.pluginEngine.RegisterCallback(self.HelloWorld, "cameraStills")

    def HelloWorld(self, cameraStills):
        print(cameraStills)
