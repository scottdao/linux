# !/bin/bash

# mytest

case $1 in
	start)
		echo 'start'
		;;
	stop)
		echo 'stop'
		;;
	restart) 
		echo 'restart'
		;;
	*)
		echo 'default'
		;;
esac

