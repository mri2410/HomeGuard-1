HomeGuard
=========

To run the program, first open a terminal, create a directory and 
clone the directory in your local machine:
$ git clone https://github.com/raiarun/HomeGuard

open another terminal, cd into HomeGuard,
run $ python publisher.py

open next terminal, cd into HomeInformation,
run $ qmake
  $ make
  run the executable.
  choose email and enter your email id (phone service is not active now). Hit OK.
  
cd into VisitorMessageBox,
run $ qmake
  $ make
  run the executable.
  type a test message and hit OK.
(Qt4 should be installed before these projects are run)
Check you email, a message will be in your email inbox.

When finished, go back to terminal and enter Ctrl + c to exit the program.

