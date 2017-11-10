from PluginSystem.PluginEngine import PluginEngine

pluginEngine = PluginEngine()
pluginCallbacks = pluginEngine.GetPluginCallbacks()

# Loop through all callback functions
for function, streams in pluginCallbacks.items():

    # key is a pointer to the function
    function("Hello World")
    print(streams)

    # value[1] contains all streams that are required for this plugin function
    for stream in streams:
        print(stream)
