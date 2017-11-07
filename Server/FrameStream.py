from DataStream import *
from PIL import Image
import io
import string
import json
import subprocess
#wtf
from sys import path
from os.path import dirname as dir
path.append(dir(path[0]))
from Utils import Depacketizer

from PIL import Image

"""
A test datastream, which receives simple utf-8 data
Prints the data along with a custom message
See DefStream for its counterpart test stream
"""

class FrameStream(DataStream):

    def HandleStream(self, data):
        count = 0

        try:
            self.expectingPacket
        except:
            self.expectingPacket = False

        if not self.expectingPacket:
            jsonstr = data.decode('utf8')
            size = json.loads(jsonstr)
            print('packets', size['packets'])
            print('fsize', size['finalPacketSize'])

            self.depacketizer = Depacketizer.Depacketizer(size['packets'], size['finalPacketSize'])
            self.expectingPacket = True
        else:
            #print(len(data))
            self.depacketizer.Next(data)
            if self.depacketizer.Done():
                print('done')
                self.expectingPacket = False
                data = self.depacketizer.Data()
                print('final len', len(data))
                image = Image.open(io.BytesIO(data))
                image.save("adaf_frame.JPG")
                image.show()
                cmdline = ['alpr','adaf_frame.JPG']
                player = subprocess.Popen(cmdline, stdin=subprocess.PIPE)
