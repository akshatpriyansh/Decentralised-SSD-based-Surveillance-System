#!/usr/bin/bash
location=1
for filename in /home/osboxes/Desktop/MajorProject/ec2_files/SSD/*; do
        ./run.py --prototxt prototxt.txt --model model.caffemodel -i $filename>>output.txt
	if grep person output.txt;then
		echo "Intruder found at time ${filename:60:11} at location ${location}"
		cat output.txt > boundingbox.txt
		break
	else	
		echo "False Positive"
	fi
done

rm output.txt

