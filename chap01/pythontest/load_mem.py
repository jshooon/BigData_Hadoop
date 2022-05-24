#! /usr/bin/python3

with open('members.txt', 'r') as fin:
	for line in fin:
		if len(line) < 2:
			break
		num, name, phone = line.split()
		str = "{}\t{}\t{}".format(num,name,phone)
		print(str)
