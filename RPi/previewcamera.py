import numpy as np
from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.hflip = True
camera.vflip = True
camera.start_preview(alpha=255)
sleep(20)

for i in range(5):
    camera.capture('/home/pi/Documents/captsone_pi/images/image%s.jpg' % i)

camera.stop_preview()
