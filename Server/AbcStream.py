from DataStream import *

"""
A test datastream, which receives simple utf-8 data
Prints the data along with a custom message
See DefStream for its counterpart test stream
"""
class AbcStream(DataStream):

    def HandleStream(self, data):
        message = data.decode('utf8')
        print('AbcStream got a message:', message)
