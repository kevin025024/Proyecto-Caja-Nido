from picamera import PiCamera
from time import sleep
import requests
camera = PiCamera()
for i in range(10):
       camera.capture(f"./foto{i}.jpg") 
       files = {'file': open(f'./foto{i}.jpg', 'rb')}
       print(requests.post(url='http://10.9.121.15:5000/uploader', files=files))