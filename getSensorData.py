


import time

def getSensorData(object):
	print 'Visiter message received'
	while object.getLoopState():
		time.sleep(1)
		print 'Sensor Loop'
