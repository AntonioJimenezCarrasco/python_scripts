#!/bin/python3

import sys
import socket
from datetime import datetime

#Define the target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #This translates hostname to IPv4
else:
	print("Invalid amount of arguments.") #Error message
	print("Syntax: python3 portscanner.py <ip>") #Valid input example
	
#Banner
print("-" * 50)
print("Scanning target "+ target)
print("Time started: "+str(datetime.now()))
print("-" * 50)

try:
	for port in range (50, 85): #Set the range of ports to scan through. Not threading, it is slow
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET = IPv4, STREAM = port
		socket.setdefaulttimeout(1) #Stops trying to connect to a port after 1 second
		result = s.connect_ex((target, port)) #Returns an error indicator
		print("Checking port {}...".format(port))
		if result == 0:
			print("The port {} is open.".format(port))
		s.close #Closes de conection
		
except KeyboardInterrupt:
	print("\nExiting program.") #Control + C
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved.") #DNS failure
	sys.exit()
	
except socket.error:
	print("Couldn't connect to the server.")
	sys.exit()
	
#It does not prevent you from using IPs that do not exist
#TCM PEH Course, modified version
