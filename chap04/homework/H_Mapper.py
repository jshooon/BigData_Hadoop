#! /usr/bin/python3

import sys
items = ['Sell', 'List', 'Living', 'Rooms', 'Beds', 'Baths', 'Age', 'Acres', 'Taxes']
for line in sys.stdin:
	line = line.strip()
	values = line.split(',')
	for i in range(0,len(values)):
		try:
			num = int(values[i].strip())
		except:
			continue
		print("{}\t{}".format(num,items[i]))
