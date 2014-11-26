
# Created by Arun Rai
# 11/25/2014

import time

""" Receive the host user information from the GUI
and ave the information """

def infoSetup(setHostInfo, message):
	print 'Host info setup message received'
	if message[0] == '<' and message[1] == '<' and message[2] == '<':
		email = message[3:len(message)]
		""" This is an email id of the host user. """
		setHostInfo.setEmail(email);
	elif message[0] == '>' and message[1] == '>' and message[2] == '>':
		phone = message[3:len(message)]
		""" This is a phone number of the the host user. """
		setHostInfo.setPhoneNumber(phone);
	elif message[0] == '-' and message[1] == '-' and message[2] == '-':
		extractMessage = message[3:len(message)]
		i = 0; loop = True;
		email = '' ; phone = ''
		while (loop):
			if extractMessage[i] == '+':
				loop = False
			else:
				email = email + extractMessage[i];
				i +=1;
		phone = extractMessage[(i + 1):len(extractMessage)];
		""" Both email id and phone number of the host user.
		the user wants to receive messages through both media."""
		setHostInfo.setBoth(email, phone);
