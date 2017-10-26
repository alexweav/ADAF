# Needed for loading from directory
import sys
from os import listdir
from os.path import isfile, join
from importlib import import_module

# Added path to plugins package TODO This needs to be updated to work in any sys
sys.path.insert(0, '/Users/mario/developer/python/ADAF/plugins')


"""
Plugin Engine
On init the engine will load all the modules inside of the plugins
directory and add them to the list of available classes stored in PluginBase.
"""
class PluginEngine:

    def __init__(self):
        print("Loading Directory")
        self.loadFromDirectory("../plugins")

    def loadFromDirectory(self, folderPath):

        # get a list of modules from the plugins directory
        folder = [f for f in listdir(folderPath) if isfile(join(folderPath, f))]
        print("Files in Plugin folder: ", folder)
        print("First Module: ", folderPath + "/" + folder[0])

        relativeModule = import_module("testPlugin", "plugins/")
        test2 = relativeModule.HelloWorldPlugin()
        test2.helloWorld()

        # my_module = import_module(folderPath + "/" + folder[0], folder[0])


        # print("OnlyFiles", onlyfiles)
        # for file in folder:
        #     print(file)
        #     modules = map(__import__, moduleNames)
        #     x = createClassFromFile()
        #     self.callback.add(class.getCallBack)


plugin = PluginEngine()

"""
Plugin Base
TODO: Write short description
"""
class PluginBase:
    availableClasses = []

    def __init__(self):
        registerCallback(callback)

    def registerCallbacks(args):
        return 0

    def getCallBacks():
        return 1
