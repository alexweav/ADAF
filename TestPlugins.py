from PluginSystem.PluginEngine import PluginEngine

pluginEngine = PluginEngine()
pluginCallbacks = pluginEngine.GetPluginCallbacks()

# Loop through all callback functions
for function, stream in pluginCallbacks.items():

    # key is a pointer to the function
    function("Hello World")
    print(stream)
