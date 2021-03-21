import RPi.GPIO as GPIO          
from time import sleep

in11 = 4
in12 = 18
ena = 23
in21 = 27
in22 = 17
enb = 24
temp1=1

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(in11,GPIO.OUT)
GPIO.setup(in12,GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)
GPIO.setup(in21,GPIO.OUT)
GPIO.setup(in22,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)

GPIO.output(in11,GPIO.LOW)
GPIO.output(in12,GPIO.LOW)
GPIO.output(in21,GPIO.LOW)
GPIO.output(in22,GPIO.LOW)
p1=GPIO.PWM(ena,100)
p2=GPIO.PWM(enb,100)
p1.start(25)
p2.start(25)
print("\n")
print("Padrão da velocidade e direção é devagar e frente")
print("e-start q-stop w-frente s-atras v-devagar f-medio r-rapido t-sair")
print("\n")    

while(1):

    x=raw_input()
    
    if x=='e':
        print("rodando")
        if(temp1==0):
            GPIO.output(in11,GPIO.LOW)
            GPIO.output(in12,GPIO.LOW)
            GPIO.output(in21,GPIO.LOW)
            GPIO.output(in22,GPIO.LOW)
            print("parado")
            x='z'
        elif(temp1==1):
            GPIO.output(in11,GPIO.HIGH)
            GPIO.output(in12,GPIO.LOW)
            GPIO.output(in21,GPIO.HIGH)
            GPIO.output(in22,GPIO.LOW)
            print("frente")
            x='z'
        elif(temp1==2):
            GPIO.output(in11,GPIO.LOW)
            GPIO.output(in12,GPIO.HIGH)
            GPIO.output(in21,GPIO.LOW)
            GPIO.output(in22,GPIO.HIGH)
            print("atras")
            x='z'
        elif(temp1==3):
            GPIO.output(in11,GPIO.LOW)
            GPIO.output(in12,GPIO.HIGH)
            GPIO.output(in21,GPIO.HIGH)
            GPIO.output(in22,GPIO.LOW)
            print("esquerda")
            x='z'
        elif(temp1==4):
            GPIO.output(in11,GPIO.HIGH)
            GPIO.output(in12,GPIO.LOW)
            GPIO.output(in21,GPIO.LOW)
            GPIO.output(in22,GPIO.HIGH)
            print("direita")
            x='z'
        

    elif x=='e':
        print("parou")
        GPIO.output(in11,GPIO.LOW)
        GPIO.output(in12,GPIO.LOW)
        GPIO.output(in21,GPIO.LOW)
        GPIO.output(in22,GPIO.LOW)
        temp1=0
        x='z'

    elif x=='w':
        print("frente")
        GPIO.output(in11,GPIO.HIGH)
        GPIO.output(in12,GPIO.LOW)
        GPIO.output(in21,GPIO.HIGH)
        GPIO.output(in22,GPIO.LOW)
        temp1=1
        x='z'

    elif x=='s':
        print("atras")
        GPIO.output(in11,GPIO.LOW)
        GPIO.output(in12,GPIO.HIGH)
        GPIO.output(in21,GPIO.LOW)
        GPIO.output(in22,GPIO.HIGH)
        temp1=2
        x='z'
    
    elif x=='a':
        print("esquerda")
        GPIO.output(in11,GPIO.LOW)
        GPIO.output(in12,GPIO.HIGH)
        GPIO.output(in21,GPIO.HIGH)
        GPIO.output(in22,GPIO.LOW)
        temp1=3
        x='z'
    
    elif x=='s':
        print("direita")
        GPIO.output(in11,GPIO.HIGH)
        GPIO.output(in12,GPIO.LOW)
        GPIO.output(in21,GPIO.LOW)
        GPIO.output(in22,GPIO.HIGH)
        temp1=4
        x='z'
    
    elif x=='v':
        print("devagar")
        p1.ChangeDutyCycle(25)
        p2.ChangeDutyCycle(25)
        x='z'

    elif x=='f':
        print("medio")
        p1.ChangeDutyCycle(50)
        p2.ChangeDutyCycle(50)
        x='z'

    elif x=='r':
        print("rapido")
        p1.ChangeDutyCycle(75)
        p2.ChangeDutyCycle(75)
        x='z'
    
    elif x=='t':
        GPIO.cleanup()
        print("GPIO Clean up")
        break
    
    else:
        print("erro")

