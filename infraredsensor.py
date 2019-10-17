import RPi.GPIO as GPIO
import time

signal = 12
light = 16


def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(signal,GPIO.IN)
    GPIO.setup(light,GPIO.OUT)
    pass


def detct():
    while True:
        if GPIO.input(signal) == 1:
            GPIO.output(light,GPIO.LOW)
            print ('lighting')
            time.sleep(20)
            GPIO.output(light,GPIO.HIGH)
            time.sleep(10)
        elif GPIO.input(signal) == 0:
            GPIO.output(light,GPIO.HIGH)
            print ('nobody')
    time.sleep(6)


#time.sleep(6)
init()
detct()
GPIO.cleanup()

