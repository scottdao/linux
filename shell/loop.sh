
# !/bin/bash

# num=3
# tot=0
# while [ $num -gt 0 ]

# do 
# 	tot=$[$tot+$num]
# 	num=$[$num-1]	
# done
# 	echo $tot

# 隔行换色

i=0;
while [ $i -lt 10 ]
do
	if [ $[$i%2] -eq 0 ]

	then
		echo -e  "\033[37;40m${i}\033[0m"
	else
			echo $i
	fi

		i=$[ $i+1 ]
done
