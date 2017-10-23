from DataStream import *

"""
A test datastream, along with AbcStream
Takes simple utf-8 data. Prints it with a custom message
"""
class DefStream(DataStream):

    def HandleStream(self, data):
        message = data.decode('utf8')
        print('DefStream got its own separate message:', message)
