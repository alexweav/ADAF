import json
from DataStream import *

class UninitializedStream(DataStream):
    
    def HandleStream(self, data):
        jsonstr = data.decode('utf8')
        identifier = json.loads(jsonstr)
        stream_type = identifier['type']
        if stream_type == 'AbcStream':
            print('AbcStream requested')
