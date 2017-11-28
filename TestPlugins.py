from PluginSystem.PluginEngine import PluginEngine

pluginEngine = PluginEngine()
pluginCallbacks = pluginEngine.GetPluginCallbacks()

pluginEngine.ExecutePlugin("FrameStream", "the requested data passed in")
