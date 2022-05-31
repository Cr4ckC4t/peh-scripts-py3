#!/usr/bin/env python3

import sys

# List of nown bad characters (in string format like: "05")
expectedbad = ['00']

# Follow ESP in dump -> mark the bad_char_payload and paste it here
dump = r"""
"""

# Extract bytes
dump = dump.split('\n')[1:-1]
dump = ' '.join([l[10:33] for l in dump]).split()

# Create hex array
h = [f'{x:02X}' for x in range(0,256)]

# Unify expected bad characters
expectedbad = [b.upper() for b in expectedbad]

# Remove known bad chars
h = list(filter(lambda x: x.upper() not in expectedbad, h))

# Colors
class fc:
        cyan    = '\033[96m'
        green   = '\033[92m'
        orange  = '\033[93m'
        red     = '\033[91m'
        redbg   = '\33[41m'
        end     = '\033[0m'
        bold    = '\033[1m'

print(f'Attempting to find {fc.redbg}bad{fc.end} characters.')

# Compare bytes up to the first difference
for i in range(min(len(dump), len(h))):
	if dump[i] != h[i]:
		print(f'{fc.orange}Found new bad character.{fc.end}')
		print(f'Expected {fc.cyan}{h[i]}{fc.end} but dump contained {fc.red}{dump[i:i+2]}{fc.end} at offset {fc.orange}{i}{fc.end}')
		expectedbad.append(h[i])
		break

print(f'{fc.green}Matching complete.{fc.end}')
print(f'List of all bad characters: {fc.orange}{expectedbad}{fc.end}')
