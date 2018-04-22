# Decentralised-SSD-based-Surveillance-System
An AWS based Surveillance system utilizing SSD and Activity recognition to detect motion in images and upload data to s3, to be fetched from EC2 servers running on AWS.

EC2 instances do the work of off-premises processing and basically run the SSD model.
Automation is done through cron scripts
#
EC2 Side

1.	sudo yum –y update
2.	sudo pip install opencv-python
3.	sudo pip install boto3
4.	aws configure – region is ap-south-1
5.	wget <link-of-project>
6.	touch ~/email.txt
7.	open email.txt and add these lines

	Subject: Intruder Detected at Your House

This mail is to notify you that an intruder has been detected at your house

8.	open crontab –e and add the crontab data from crontab.txt to start the EC2-Program
#
Machine Side

1.	add crontab through crontab –e from the file crontab.txt
2.	bash initialize.sh 


#General Information

Data is being pumped from Machine to S3 at rate of – 15 seconds/iteration of EC2 crontab script

Data is being ingested for S3 to EC2 at the rate of – 5 seconds/iteration of Machine crontab script
