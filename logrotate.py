#!/usr/bin/env python3


import glob
import os.path


print("hello")


pattern = "tmp/*"
for f_name in glob.glob(pattern) :
	print(f_name)
	print(os.path.getsize(f_name))

	#pseudo algo
	#list files
	#find head
	#check head size
	#maybe rotate
	#maybe trim tail

