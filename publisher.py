"""
ECE 4564
Final Project
Team: Immortal
Title: HomeGuard - Home Visitors Detection and Alert System
Filename: publisher.py
Members: Arun Rai, Mohammad Islam, and Yihan Pang
Date: 11/26/2014

---------------------------------------------------------------------
Description:
1. Receive host user information.
2. Receive visitors' message.
3. Receive sensor reading, and send trigger signal to camera.

Network protocols: TCP/IP and AMQP
---------------------------------------------------------------------
"""

#!/usr/bin/python

import sys
import threading
from infoSetup import infoSetup
from getSensorData import getSensorData
from getVisitorMessage import getVisitorMessage
import time
import signal
import socket

""" Default host IP address and port number """
HOST = "127.0.0.1"
PORT = 9000

class HostInformation:
	def __init__(self):
		self.senderPhoneNumber = '';
		self.receiverPhoneNumber = ''
		self.sender = 'homeguard96@gmail.com';
		self.password = 'detectionsystem'
		self.receiverEamil = 'sangpang20@gmail.com';
		self.twilloID = ''
		self.twilloPass = ''
		self.loop = True;
		self.s = '';
		self.emailOnly = True;
		self.smsOnly = False;
		self.both = False;
		
	def setPhoneNumber(self, number):
		self.receiverPhoneNumber = number;
		self.smsOnly = True;
		self.emailOnly = False;
		self.both = False;
		
	def setEmail(self, email):
		self.receiverEamil = email;
		self.emailOnly = True;
		self.smsOnly = False;
		self.both = False;
		
	def setBoth(self, email, phone):
		self.receiverEamil = email;
		self.receiverPhoneNumber = phone;
		self.both = True;
		self.emailOnly = False;
		self.smsOnly = False;
		
	def getSenderPhoneNumber(self):
		return self.senderPhoneNumber;
		
	def getReceiverPhoneNumber(self):
		return self.receiverPhoneNumber;
		
	def getReceiverEmail(self):
		return self.receiverEamil;
		
	def getSenderEmail(self):
		return self.sender;
		
	def getSenderEmailPass(self):
		return self.password;
		
	def messageInEmail(self):
		return self.emailOnly;
		
	def messageInSms(self):
		return self.smsOnly;
		
	def messageInBoth(self):
		return self.both;
		
	def getTwilloID(self):
		return self.twilloID;
		
	def getTwilloPass(self):
		return self.twilloPass;
		
	def setLoopState(self, signal=None, frame=None):
		print 'Gracefully closing the socket .................'
		self.loop = False;
		self.s.close();
		
	def getLoopState(self):
		return self.loop;
	
	def closeSocket(self, s):
		self.s = s;


def main():
	setHostInfo = HostInformation()
	sensorThread = threading.Thread(target = getSensorData, args = [setHostInfo,]);
	
	sensorThread.start()
	signal_num = signal.SIGINT
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.bind((HOST, PORT))
		s.listen(1)
		while setHostInfo.getLoopState():
			try:
				setHostInfo.closeSocket(s);
				signal.signal(signal_num, setHostInfo.setLoopState)
				signal_num = signal.SIGTERM
				signal.signal(signal_num, setHostInfo.setLoopState)
			except ValueError as error1:
				print "Warning: Greceful shutdown may not be possible: Unsupported"
				print "Signal: " + signal_num
			
			conn, addr = s.accept()
			message = conn.recv(1024)
			if len(message) > 3:
				if message[0] == '$' and message[1] == '$' and message[2] == '$':
					getVisitorMessage(setHostInfo, message)
				else:
					infoSetup(setHostInfo, message)
		
	except socket.error, se:
		print 'connection failed/socket closed. \n', se
		if s:
			s.close();
			
	sensorThread.join()
	
if __name__ == '__main__':
	main();

