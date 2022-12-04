import RPi.GPIO as GPIO
from time import sleep

dir = 23
pwm = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(dir, GPIO.OUT)
GPIO.setup(pwm, GPIO.OUT)

p = GPIO.PWM(pwm, 1000)
p.start(50)

GPIO.output(dir, GPIO.HIGH)
sleep(10)
GPIO.cleanup()
