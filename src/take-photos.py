import cv2
camera = cv2.VideoCapture(0)
for i in range(10):
    ret, image = camera.read()
    fileimage = open(f"{i}.jpg", wb)
        