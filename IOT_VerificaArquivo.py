import RPi.GPIO as GPIO
import time
import os.path

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
while True:
    if os.path.exists('/home/pi/Desktop/teste/1.txt'): 
        print ("LED Azul ligado")
        GPIO.output(18,GPIO.HIGH)
        GPIO.output(15,GPIO.LOW)
        time.sleep(2)
    else:
        print ("LED verde ligado")
        GPIO.output(18,GPIO.LOW)
        GPIO.output(15,GPIO.HIGH)
        time.sleep(2)   
