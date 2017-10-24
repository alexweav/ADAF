from DataStream import *
from PIL import Image
import io
import string

"""
A test datastream, which receives simple utf-8 data
Prints the data along with a custom message
See DefStream for its counterpart test stream
"""

class FrameStream(DataStream):
    
    def HandleStream(self, data):
        count = 0
        
        print(len(data))
        for b in data:
            print(b)
            count = count +1
            if count > 5:
                break
    #image = Image.open(io.BytesIO(data))
    #image.show()
    #print('Image is %dx%d' % image.size)
        #image.verify()
        # print('Image is verified')
#print('FrameStream got a message:', message)
