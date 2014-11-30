import time
import pika
import json
import signal
import os
import RPi.GPIO as GPIO
import time
def getSensorData(object):
	while object.getLoopState():
		time.sleep(1)
		if object.getMessageSignal() == True:
			print 'Visiter message received'
			message = json.dumps(object.getMessage(), indent = 2)
			print message
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
