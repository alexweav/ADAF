import json
from DataStream import *
from AbcStream import *

class UninitializedStream(DataStream):
    
    def HandleStream(self, data):
        jsonstr = data.decode('utf8')
        identifier = json.loads(jsonstr)
        stream_type = identifier['type']
        if stream_type == 'AbcStream':
            print('AbcStream requested')
            stream = AbcStream(self.address, self.socket, self.registry)
        elif stream_type == 'DefStream':
            print('DefStream requested')
        else:
            print('An unrecognized stream attempted to connect. Closing...')
            self.Close()
        return stream
