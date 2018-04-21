#!/bin/bash
location=1
for filename in /home/ec2-user/MajorProject/ec2_files/s3_files/*; do
        /home/ec2-user/MajorProject/ec2_files/SSD/run.py --prototxt /home/ec2-user/MajorProject/ec2_files/SSD/prototxt.txt --model /home/ec2-user/MajorProject/ec2_files/SSD/model.caffemodel -i $filename>>output.txt
	echo  "File metadata :::::: "$filename
	if grep person output.txt;then
		echo "Intruder found at time ${filename:60:11} at location ${location}"
		/usr/sbin/sendmail mayankvarmaftw@gmail.com < /home/ec2-user/email.txt
		cat output.txt > boundingbox.txt
		break
	else	
		echo "False Positive"
	fi
done

rm output.txt
