import plugin.py

"""
This plugin has one function, which returns the text "Hello World"
"""
class HelloWorldPlugin(PluginBase):

    def __init__(args, PluginBase):
        PluginBase.RegisterCallback("do shit")

    def helloWorld():
        return "hello world"
