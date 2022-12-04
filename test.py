from picamera import PiCamera
from time import sleep

with PiCamera() as camera:
    camera.rotation = 180
    camera.start_preview()
    sleep(10)
    camera.stop_preview()
