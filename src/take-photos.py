from picamera import PiCamera
from time import sleep
camera = PiCamera()
for i in range(10):
       camera.capture(f"./foto{i}.jpg") 
