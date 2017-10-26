# Needed for loading from directory
import sys
import os
from os import listdir
from os.path import isfile, join
from importlib import import_module

"""
Plugin Engine
On init the engine will load all the modules inside of the plugins
directory and add them to the list of available classes stored in PluginBase.
"""
class PluginEngine:

    def __init__(self):
        # Sets the plugins package path
        pluginPath = self.setPluginsDirectoryPath()
        self.loadFromDirectory(pluginPath + "/plugins")

    """
    Returns the path for the plugins directory and adds it to sys.path to make it a
    package that may be referenced from an import statement.
    """
    def setPluginsDirectoryPath(self):
        # __file__ : this file path, relative to os.getcwd()
        # full_path : This file full path (following symlinks)
        full_path = os.path.realpath(__file__)

        # os.path.dirname(full_path) : This file directory only
        # sys.path.insert : Inserts path into the sys.path to add plugins as a package
        sys.path.insert(0, os.path.dirname(os.path.dirname(full_path)) + "/plugins")
        return os.path.dirname(os.path.dirname(full_path))

    """
    Loads all the plugin modules
    """
    def loadFromDirectory(self, folderPath):
        # get a list of modules from the plugins directory
        plugins = [f for f in listdir(folderPath) if isfile(join(folderPath, f))]
        print("Files in Plugin folder: ", plugins)
        print("First Module: ", folderPath + "/" + plugins[0])

        moduleList = []
        ignoreFiles = [".DS_Store", "__init__.py"]
        print("Plugins: ", plugins)

        module = import_module("testPlugin", "plugins/")
        print(module)

        for plugin in plugins:
            # Check for system files
            if(plugin in ignoreFiles):
                continue

            # Checks for .py at the end of module names
            if plugin.endswith('.py'):
                plugin = plugin[:-3]

            # Imports the module
            module = import_module(plugin, "plugins/")
            moduleList.append(module)

        print(moduleList)

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
