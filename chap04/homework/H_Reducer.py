#! /usr/bin/python3

import sys

items = {'Sell':[], 'List':[], 'Living':[], 'Rooms':[], 'Beds':[], 'Baths':[], 'Age':[], 'Acres':[], 'Taxes':[]}
beds = {'three_beds':[]}
sell = []
for line in sys.stdin:
	line = line.strip()
	a,b = line.split('\t',1)
	items[b.strip()].append(int(a.strip()))

for i in range(0,len(items['Beds'])):
	if items['Beds'][i] == 3:
		sell.append(items['Sell'][i])
		beds['three_beds'].append(int(items['Beds'][i]))

print('minsell : ', min(sell))
print('maxsell : ', max(sell))
