# Needed for loading from directory
from os import listdir
from os.path import isfile, join

"""
Plugin Engine
TODO: Write short description
"""
class PluginEngine:

    def __init__(args):
        LoadFromDirectory("../plugins")


"""
Plugin Base
TODO: Write short description
"""
class PluginBase:
    def __init__(args):
        RegisterCallback(callback)

    def RegisterCallbacks(args):
        return 0

    def getCallBacks():
        return 1
