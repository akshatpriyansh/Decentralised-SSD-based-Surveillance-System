#!/bin/bash

python /home/ec2-user/MajorProject/ec2_files/get_from_s3.py
python /home/ec2-user/MajorProject/ec2_files/shift_s3_files_to_folder.py
bash /home/ec2-user/MajorProject/ec2_files/mainfile.sh
python /home/ec2-user/MajorProject/ec2_files/delete.py
