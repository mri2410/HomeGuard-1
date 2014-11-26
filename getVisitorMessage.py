
# Created by Arun Rai
# 11/25/2014

import socket
import sys
from smsAndEmailToHost import sendEmailToHost

""" Receive the visitor's message and send it to host
via email or/and phone (as setup by the host user)"""
def getVisitorMessage(setHostInfo, message):
	visitorMsg = message[3:len(message)]
	host = 'smtp.gmail.com'
	port = '587'
	if setHostInfo.messageInBoth():
		print 'both way'
	else:
		if setHostInfo.messageInEmail():
			print 'sending message in email'
			sendEmailToHost(host, port, setHostInfo.getSenderEmail(), setHostInfo.getSenderEmailPass(), 
						setHostInfo.getReceiverEmail(), visitorMsg)
		elif setHostInfo.messageInSms():
			print 'sending message in phone'
	
			
