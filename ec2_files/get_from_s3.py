#!/usr/bin/python

"""
this is file is used to download all files from s3
"""

import boto3

name1='chaturbucket-1'
name2='chaturbucket-2'
s3 = boto3.resource('s3')
bucket1 = s3.Bucket(name1)
bucket2 = s3.Bucket(name2)

i=1;
j=1;

try:
	print("Listing all items currently in bucket 1..........")
	for obj in bucket1.objects.all():

		file=str(obj.key)
		s3.Bucket(name1).download_file(obj.key,file)
		print("%d:"%i +" "+ obj.key)
		i=i+1
                obj.delete()	
	print("Listing all items currently in bucket 2..........")
	for obj in bucket2.objects.all():
		
		file=str(obj.key)
		s3.Bucket(name2).download_file(obj.key,file)
		print("%d:"%j +" "+obj.key)
		j=j+1
                obj.delete()
except:
	print("error")
