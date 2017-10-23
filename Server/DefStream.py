from DataStream import *

class DefStream(DataStream):

    def HandleStream(self, data):
        message = data.decode('utf8')
        print('DefStream got its own separate message:', message)
