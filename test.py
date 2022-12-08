from picamera import PiCamera
from time import sleep

def main():
    with PiCamera() as camera:
        camera.rotation = 180
        camera.start_preview()
        sleep(10)
        camera.stop_preview()

if __name__ == '__main__':
    main()
