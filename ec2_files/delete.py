#!/usr/bin/python

import os
path='/home/ec2-user/MajorProject/ec2_files/s3_files/'
if(os.listdir(path)):
	for item in os.listdir(path):
		os.remove(path+item)

