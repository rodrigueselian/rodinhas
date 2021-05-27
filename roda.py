import RPi.GPIO as GPIO          
from time import sleep
import time

in11 = 4
in12 = 18
ena = 23
in21 = 27
in22 = 17
enb = 24
TRIG = 5
ECHO = 6


GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(in11,GPIO.OUT)
GPIO.setup(in12,GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)
GPIO.setup(in21,GPIO.OUT)
GPIO.setup(in22,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(in11,GPIO.LOW)
GPIO.output(in12,GPIO.LOW)
GPIO.output(in21,GPIO.LOW)
GPIO.output(in22,GPIO.LOW)
p1=GPIO.PWM(ena,100)
p2=GPIO.PWM(enb,100)
p1.start(50)
p2.start(50)

def get_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.0001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == False:
        start = time.time()
    while GPIO.input(ECHO) == True:
        end = time.time()
    sig_time = end-start
    distance = sig_time / 0.000058
    return distance

def move():
    GPIO.output(in11,GPIO.HIGH)
    GPIO.output(in12,GPIO.LOW)
    GPIO.output(in21,GPIO.HIGH)
    GPIO.output(in22,GPIO.LOW)

def left():
    GPIO.output(in11,GPIO.LOW)
    GPIO.output(in12,GPIO.HIGH)
    GPIO.output(in21,GPIO.HIGH)
    GPIO.output(in22,GPIO.LOW)

while(1):
    distance = get_distance()
    time.sleep(0.1)
    if distance > 10:
        move()
    else:
        left()
