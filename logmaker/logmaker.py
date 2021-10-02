#!/usr/bin/env python3


print("hello")

import time

total_counter = 0

import sys

rate = int(open("rate", "r").read())
tick = 1.0



while True:

	last_tick = time.time()
	for i in range(rate) :
		print("Line %u" % total_counter)
		total_counter += 1

	now = time.time()
	print_duration = now - last_tick
	if print_duration < tick :
		sleep_duration = tick - print_duration
		print("waiting for %.3f" % sleep_duration)
		print("thats a potential max rate of %.1f lines/s" % (rate / print_duration), flush = True)
		time.sleep(sleep_duration)





