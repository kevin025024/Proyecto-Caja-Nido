from picamera import PiCamera
import time
import RPi.GPIO as GPIO
import requests

camera = PiCamera()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
PIR_PIN = 23
GPIO.setup(PIR_PIN, GPIO.IN)

print('iniciando el modulo sensor PIR (clickea parar para salir)')
print ('Listo')

while True:
  if GPIO.input(PIR_PIN):
    print('Movimiento detectado')
    camera.capture(f"./foto.jpg") 
    files = {'file': open(f'./foto.jpg', 'rb')}
    print(requests.post(url='http://10.9.121.208:5000/uploader', files=files))  
  time.sleep(1)