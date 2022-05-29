#!/usr/bin/env python3

import sys
import socket
from datetime import datetime as dt


def main(ip):
	try:
		target = socket.gethostbyname(ip)
	except:
		print(f'Failed to get host by name')
		sys.exit(1)

	# Banner
	print(f'{"-"*60}')
	print(f'\tScanning target : {target}')
	print(f'\tTime started    : {dt.now()}')
	print(f'{"-"*60}')

	try:
		socket.setdefaulttimeout(0.2)
		for port in range(30,90):
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			result = s.connect_ex((target, port)) # returns an error indicator

			if result == 0:
				print(f'Port {port:5} is open')
			s.close()

	except KeyboardInterrupt:
		print(f'\nExiting program')
		sys.exit(1)

	except socket.gaierror:
		print(f'Hostname could not be resolved')
		sys.exit(1)

	except socket.error:
		print(f'Couldn\'t connect to server')
		sys.exit(1)

	except Exception as e:
		print(f'Encountered unexpected error: {e}')
		sys.exit(1)

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print(f'\n\tUsage: {sys.argv[0]} <ip>')
		sys.exit(1)
	main(sys.argv[1])
