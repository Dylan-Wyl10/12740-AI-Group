# -*- coding: utf-8 -*
import time
import dht11
import RPi.GPIO as GPIO
import numpy as np

#define GPIO 14 as DHT11 data pin
Temp_sensor=14
def main():
  # Main program block
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
	instance=dht11.DHT11(pin = Temp_sensor)
	data=[]

	while True:
		result=instance.read()
		data.append((result.temperature,result.humidity))
		time.sleep(3)
		if result.temperature == 0 or result.humidity == 0:
			continue
		else:
			print"Temperature = ",result.temperature,"C"," Humidity = ",result.humidity,"%"

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		pass
