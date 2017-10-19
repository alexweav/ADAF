from DataStream import *

class AbcStream(DataStream):
    
    def HandleStream(self, data):
        message = data.decode('utf8')
        print('AbcStream got a message:', message)
