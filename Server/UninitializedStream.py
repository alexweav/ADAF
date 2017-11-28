import json
from DataStream import *
from AbcStream import *
from DefStream import *
from FrameStream import *

class UninitializedStream(DataStream):
    
    def HandleStream(self, data):
        jsonstr = data.decode('utf8')
        identifier = json.loads(jsonstr)
        stream_type = identifier['type']
        if stream_type == 'AbcStream':
            print('AbcStream requested')
            stream = AbcStream(self.address, self.socket, self.registry, 'AbcStream')
        elif stream_type == 'DefStream':
            print('DefStream requested')
            stream = DefStream(self.address, self.socket, self.registry, 'DefStream')
        elif stream_type == 'FrameStream':
            print('FrameStream requested')
            stream = FrameStream(self.address, self.socket, self.registry, 'FrameStream')
        else:
            print('An unrecognized stream attempted to connect. Closing...')
            self.Close()
        return stream
