
# !/bin/bash

read -p 'name:' name

read -p 'password:' passwd

if [ $name = 'ldy' ] && [ $passwd = '123456' ]
then 
	echo '登陆成功！'
else 
	echo '登陆失败！'
fi

