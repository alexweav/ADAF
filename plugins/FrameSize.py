from sys import path
from os.path import dirname as dir
path.append(dir(path[0]))
from PluginSystem import PluginBase

"""
Plugin which prints the size of each frame
"""
class FrameSize(PluginBase.PluginBase):

    def init(self):
        self.pluginEngine.RegisterCallback(self.Print, "FrameStream")

    def Print(self, data):
            print('Frame size: ', len(data))
