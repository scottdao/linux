# !/bin/bash

# week=7
# date = date + %w
 
# week=`date +%w`


# case $week in
# 	1)
# 		echo 'work'
# 		;;
# 	2)
# 	       echo 'work2'	
# 		;;
# 	3) 
# 	       echo 'work3'

# 	       ;;
# 	*) 
# 		echo "$week"
# 		;;
# esac	       


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
	esac

