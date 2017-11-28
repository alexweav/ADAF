from sys import path
from os.path import dirname as dir
path.append(dir(path[0]))
from PluginSystem import PluginBase

from PIL import Image

"""
OpenALPR Plugin

The plugin will request framestream.
"""

class ALPRPlugin(PluginBase.PluginBase):

    def init(self):
        self.pluginEngine.RegisterCallback(self.Alpr, "FrameStream")

    def Alpr(self, data):
        print(len(data))
