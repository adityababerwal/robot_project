import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

#---ULTRASONIC SENSOR PINS------------
TRIG_FRONT_RIGHT = 13
ECHO_FRONT_RIGHT = 12
GPIO.setup(TRIG_FRONT_RIGHT, GPIO.OUT)
GPIO.setup(ECHO_FRONT_RIGHT, GPIO.IN)

TRIG_FRONT_LEFT = 8
ECHO_FRONT_LEFT = 10
GPIO.setup(TRIG_FRONT_LEFT, GPIO.OUT)
GPIO.setup(ECHO_FRONT_LEFT, GPIO.IN)

TRIG_REAR_RIGHT = 3
ECHO_REAR_RIGHT = 4
GPIO.setup(TRIG_REAR_RIGHT, GPIO.OUT)
GPIO.setup(ECHO_REAR_RIGHT, GPIO.IN)

TRIG_REAR_LEFT = 11
ECHO_REAR_LEFT = 5
GPIO.setup(TRIG_REAR_LEFT, GPIO.OUT)
GPIO.setup(ECHO_REAR_LEFT, GPIO.IN)

#--------------RELAY------------
RELAY = 999 # change
GPIO.setup(RELAY, GPIO.OUT)

#------MOTOR DRIVER PINS---------------
in1 = 3 # change
in2 = 9
en = 3 # change
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)

# define and turn on pwm
p = GPIO.PWM(en, GPIO.HIGH)
p.start(0) # initial duty cycle is 0 (on for 0% of time)

#----DEFINE KI, KP AND KD-----------------
KI = 10
KP = 10
KD = 10





















