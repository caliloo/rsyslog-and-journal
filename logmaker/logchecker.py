#!/usr/bin/env python3


print("hello")

import time

total_counter = 0

import sys

total_missed = 0
previous = -1
for l in open('/home/work/logrotate/logs/logmaker.log', 'r').readlines() :
	try :
		n = int(l.split('Line')[1])

		if n -1 != previous :
			print("skipped", previous, n , "(%u)" % (n-previous))

			total_missed += n-previous

		previous = n


	except :
		print("cant parse", l)
		continue

print("total", total_missed)


