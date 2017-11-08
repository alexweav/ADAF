from PluginSystem.PluginEngine import PluginEngine

pluginEngine = PluginEngine()
realtimeCallbacks = pluginEngine.GetRealtimeCallbacks()

for key, value in realtimeCallbacks.items():

    # value[0] is a pointer to the function
    value[0]("Hello World")

    # value[1] contains all streams that are required for this plugin function
    for streams in value[1]:
        value[0](streams)
