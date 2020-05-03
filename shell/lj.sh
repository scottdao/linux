
# !/bin/bash

# 条件测试：
# age=24

# if [ $age -lt 18 ]


# then
#        echo '未成年'
# else
#      echo '成年'
# fi     
# 分数判断:
read -p 'sco:' sco
if [ $sco -lt 60 ]
then 
	echo 'it is bad'
elif [ $sco -lt 70 ]
then
      echo 'good'
else 
  echo 'you are very good'	
fi
# 函数控制:

# 流程控制:
