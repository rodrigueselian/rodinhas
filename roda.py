import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

RODA11 = 4
RODA12 = 18
RODA21 = 27
RODA22 = 17

GPIO.setup(RODA11, GPIO.OUT)
GPIO.setup(RODA12, GPIO.OUT)
GPIO.setup(RODA21, GPIO.OUT)
GPIO.setup(RODA22, GPIO.OUT)

def foward():
    GPIO.output(RODA11, GPIO.HIGH)
    GPIO.output(RODA12, GPIO.LOW)
    GPIO.output(RODA21, GPIO.HIGH)
    GPIO.output(RODA22, GPIO.LOW)

def backward():
    GPIO.output(RODA11, GPIO.LOW)
    GPIO.output(RODA12, GPIO.HIGH)
    GPIO.output(RODA21, GPIO.LOW)
    GPIO.output(RODA22, GPIO.HIGH)

def left():
    GPIO.output(RODA11, GPIO.LOW)
    GPIO.output(RODA12, GPIO.HIGH)
    GPIO.output(RODA21, GPIO.HIGH)
    GPIO.output(RODA22, GPIO.LOW)

def right():
    GPIO.output(RODA11, GPIO.HIGH)
    GPIO.output(RODA12, GPIO.LOW)
    GPIO.output(RODA21, GPIO.LOW)
    GPIO.output(RODA22, GPIO.HIGH)

while True:
    foward()
    time.sleep(10)
    backward()
    time.sleep(10)
    left()
    time.sleep(10)
    right()
    time.sleep(10)