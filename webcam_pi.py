#! /usr/bin/env python

# Triggers the webcam after getting a signal from the publisher pi.

import sys
from subprocess import call
from time import time, sleep
import datetime

# Global variables
GIT_BASE_DIRECTORY = "./snapshots/"

# Function that triggers the webcam, takes a picture
# and names the file with date and timestamp
def snapshot():
    global GIT_BASE_DIRECTORY
    
    # Getting the year, month, day, hour, minute, and second
    currentTime = datetime.datetime.now()
    # Creating filename with the date and timestamp
    snapshotFile = "visitor_%d:%d:%d_%d:%d:%d.jpg" % \
                   (currentTime.hour, currentTime.minute,\
    		    currentTime.second, currentTime.month,\
    		    currentTime.day, currentTime.year)
    #now = datetime.datetime.now()
    #snapshotFile = "visitor-%d:%d:%d-%d:%d:%d.jpg" % (now.year, now.month, now.day, now.hour, now.minute, now.second)
    
    print "**************Taking picture**************"

    # Creating the terminal command and executing it
    snapshotCMDCommand = "fswebcam " + GIT_BASE_DIRECTORY + snapshotFile
    snapshotReturnCode = call(snapshotCMDCommand, shell = True)

    return snapshotFile    
    # Debugging 
    #print '\nTaking snapshot\n', snapshotCMDCommand
    #print  '\n', snapshotReturnCode
    

# Uploading the snapshot to the Git account
def uploadFileToGit():
    global GIT_BASE_DIRECTORY
    gitInfo = "git add " + GIT_BASE_DIRECTORY + \
                "; git commit -m " + " \"Visitor image\" " \
		+ GIT_BASE_DIRECTORY + " ; git push"

    gitReturnCode = call(gitInfo, shell=True)
    
    print "Git stuff return code is ", gitReturnCode
 

# Testing
#s = snapshot()
#print s
#uploadFileToGit()
