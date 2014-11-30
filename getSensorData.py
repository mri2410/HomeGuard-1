import time
import pika
import json
import signal
import os
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
#initial setup
TRIG = 23
ECHO = 24
#assign pins
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
signal.signal(signal.SIGUSR1,restart)
waitstart=time.time()

def getSensorData(object):
 	try:
		pause=0
		while 1:
			#reset the sensor
			GPIO.output(TRIG, False)
			time.sleep(2) 
			#trigger the sensor
			GPIO.output(TRIG, True)
			time.sleep(0.00001)
			GPIO.output(TRIG, False)	
			
			while GPIO.input(ECHO)==0:
				pulse_start = time.time()
			while GPIO.input(ECHO)==1:
				pulse_end = time.time() 
			pulse_duration = pulse_end - pulse_start
			#calculate the distance
			distance = pulse_duration * 17150
			distance = round(distance, 2)
			#if visitor isn't previous triggered 
			if pause==0 and distance>2:
				pause=1 
				waitstart=time.time()
				message = dict([])
				message['type']="trigger"
				object.setMessage(message)
				object.setMessageSignal(True)
				message = json.dumps(object.getMessage(), indent = 2)
				MessageBroker = pika.BlockingConnection(pika.ConnectionParameters(host = '127.0.0.1',
											virtual_host="mycomputer",
											credentials=pika.PlainCredentials("arun","rai",True)))
				""" Setup the exchange """
				channel = MessageBroker.channel()
				channel.exchange_declare(exchange="HomeGuard",type="fanout")

				""" Send the message """
				channel.basic_publish(exchange="HomeGuard",
							routing_key="Detection", body= message)

				""" Close the connection """ 
				MessageBroker.close()
				object.setMessageSignal(False)

			elif pause==1 and distance>400:
				pause=0
			elif time.time()-waitstart>300:
				pause=0				

			
	except KeyboardInterrupt: 
		GPIO.cleanup()
	
		
