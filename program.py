import os
import sys

for date in range(1, 26):
	try:
		os.mkdir(str(date))
	except:
		pass
	f = open(str(date) + "/program.py", "w")
	f.write("""\
import os
import sys

with open("input.txt") as file:
	lines = file.readlines()
	for line in lines:
		pass
""")

