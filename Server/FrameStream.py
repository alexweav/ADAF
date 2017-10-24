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
       
        image = Image.open(io.BytesIO(data))
            #image.verify()
            #print('Image is verified')
        image.show()
        
        #print('Image is %dx%d' % image.size)
        #print('FrameStream got a message:', message)
