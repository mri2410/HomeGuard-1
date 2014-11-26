
#!/usr/bin/python
import smtplib

""" Send message to the host via email """
def sendEmailToHost(host, port, sender, password, receiver, message = 'No message content.'):
	try:
		mail = smtplib.SMTP(host, port)
		mail.ehlo()
		mail.starttls()
		mail.login(sender, password);
		mail.sendmail(sender, receiver, message)      
		mail.close()
	except smtplib.SMTPRecipientsRefused:
		print 'Receipient refused to receive the message.'
	except smtplib.SMTPAuthenticationError:
		print 'User authentication error. \nServer did not accept username/password.'
	except smtplib.SMTPConnectError:
		print 'Unknown error while connecting to the host.'
	except Exception:
		print 'Unable to connect to the host. \nCheck the host address.'

def sendSMS(receiver, id, password, message):
	print('work to be done')
