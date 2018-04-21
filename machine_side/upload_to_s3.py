#!/usr/bin/python

import time
"""
all images in clicked_images are uploaded to s3 bucket 1
"""
import sys
import boto3
import time
import os
s3 = boto3.resource("s3")
name = 'chaturbucket-1'
syspath='/home/osboxes/Desktop/MajorProject/machine_side/clicked_images/'
try:
	for item in os.listdir(syspath):
		#object_name=item.split('.')[0]
		print("item"+item)
		response = s3.Object(name, item).put(Body=open(syspath+item, 'rb'))
		os.remove(syspath+item)
		print response
except Exception as error:
	print error
