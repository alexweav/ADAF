# Needed for loading from directory
import sys
import os
from os import listdir
from os.path import isfile, join
from importlib import import_module

"""
Plugin Engine
On init the engine will load all the modules inside of the plugins
directory and add them to the list of available classes stored in PluginManager.
"""
class PluginEngine:
    pluginCallbacks = {}

    def __init__(self):
        # Sets the plugins package path
        pluginPath = self.SetPluginsDirectoryPath()
        self.LoadFromDirectory(pluginPath + "/plugins")

    """
    Returns the path for the plugins directory and adds it to sys.path to make it a
    package that may be referenced from an import statement.
    """
    def SetPluginsDirectoryPath(self):
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
    def LoadFromDirectory(self, folderPath):
        # get a list of modules from the plugins directory
        plugins = [f for f in listdir(folderPath) if isfile(join(folderPath, f))]

        ignoreFiles = [".DS_Store", "__init__.py"]

        for plugin in plugins:
            # Check for system files
            if(plugin in ignoreFiles):
                continue

            # Checks for .py at the end of module names
            if plugin.endswith('.py'):
                plugin = plugin[:-3]

            # Imports the module
            module = import_module(plugin, "plugins/")
            myClass = getattr(module, plugin)

            # Every plugin we will pass in the engine
            instantiate = myClass(self)
            instantiate.init()

    """
    Registers the function and stream to the engine
    """
    def RegisterCallback(self, fn, stream):
        self.pluginCallbacks[fn] = stream

    """
    Returns a dictionary of all the pluginCallbacks
    """
    def GetPluginCallbacks(self):
        return self.pluginCallbacks

    """
    For a stream name and the data associated with the stream, execute all the
    functions that are requesting that stream type.
    """
    def ExecutePlugin(self, name, data):
        # Loop through all callback functions
        for function, stream in self.pluginCallbacks.items():
            if name is stream:
                function(data)
