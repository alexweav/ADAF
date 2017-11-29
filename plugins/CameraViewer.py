from sys import path
from os.path import dirname as dir
path.append(dir(path[0]))
from PluginSystem import PluginBase

from PIL import Image
import io
import string
import subprocess

"""
Plugin which simply displays images from the camera
"""
class CameraViewer(PluginBase.PluginBase):

    def init(self):
        self.pluginEngine.RegisterCallback(self.Display, "FrameStream")

    def Display(self, data):
        image = Image.open(io.BytesIO(data))
        image.show()
