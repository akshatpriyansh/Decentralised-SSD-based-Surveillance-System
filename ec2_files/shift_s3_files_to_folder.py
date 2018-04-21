#!/usr/bin/python

"""
this file is used to shift all files in current directory with extension .jpg 
to the folder s3_files
"""
import os
import shutil
# make sure that these directories exist
path='/home/ec2-user/MajorProject/ec2_files/'
dir_src = '/home/ec2-user/'
dir_dst = path+"s3_files/" 

for file in os.listdir(dir_src):
    print file  # testing
    if(file.endswith(".jpg")):
        src_file = os.path.join(dir_src, file)
        dst_file = os.path.join(dir_dst, file)
        shutil.move(src_file, dst_file)
