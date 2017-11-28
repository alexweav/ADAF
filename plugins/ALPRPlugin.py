from sys import path
from os.path import dirname as dir
path.append(dir(path[0]))
from PluginSystem import PluginBase

from PIL import Image
import io
import string
import subprocess

"""
OpenALPR Plugin

The plugin will request framestream.
"""

class ALPRPlugin(PluginBase.PluginBase):

    def init(self):
        self.pluginEngine.RegisterCallback(self.Alpr, "FrameStream")

    def Alpr(self, data):
        print('plugin got ', len(data))
        image = Image.open(io.BytesIO(data))
        image.save("adaf_frame.JPG")
        image.show()
        cmdline = ['alpr','adaf_frame.JPG']
        player = subprocess.Popen(cmdline, stdin=subprocess.PIPE)
                                                        
