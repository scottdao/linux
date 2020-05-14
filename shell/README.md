- `Bad for loop variable`: `sudo dpkg-reconfigure dash`选择否，即可；
原因:默认设置为dash，所以报错。
- `sudo apt install net-tools`:安装ip查看工具；
- zsh:命令别名；alias
- 别名长期使用：存放在.bashrc内；
- 命令重定向：bash重定向，输入到命名的文件里。
 1. >:`ifconfig eth0 > if.txt;`表示覆盖；
 2. 1>:正确重定向；2>:错误重定向；
 3. >>:追加式重定向；
 4. &>: 正确错误覆盖重定向；
- bash:管道操作：
+ **用户与权限**：`ls -l file`
  - r:读；w:写；x:执行；
  - linux用户：所有者(u)，所属组(g)，其他用户(o),所有用户(a)；
  -  文件权限：
      -  -rw-r--r-- 1 root root  0 oct 19 12:21 shell.txt
        1. 所有者（root用户）对shell.txt具有rw（读写）权限
        2.  所属者（root组内用户）对shell.txt具有r(只读)的权限
        3. 其他用户(root以外用户)对shell.txt具有r(只读)权限
  - 用户管理:
    - 查看用户：id root
    - 用户添加：`useradd  name`
    - 用户删除:`userdel  -r  name`
    - 把用户加入组:`gpasswd  -a user1 root`;
    - 把组中的用户删除: `gpasswd -d user1 root`
  - 用户与文件关系
    - chmod分配权限
      - chmod 755 file
      - chmod u+x file:通过加减进行修改文件权限
        1. 用户user1和用户user2两个用户，user1对root下的a.txt文件有读写权限，user2对root下不具备读写权限，如何操作：***先将user1加入到root组，use2不加入；在对文件a.txt赋予root组内具有读写权限。**
        `gpasswd -a user1 root`; `chmod g+w a.txt`
        2. chmod 数字权限分配：r ,4; w,2; x,1;  755 rwxr-xr-- ; 最高为7=4+2+1,最小为0;
        **注：**数字分配和命令各区所需。
        3. 权限细化需求：
              -  user1 file rw
              - user2 file rw
    - acl 权限分配
       1. setfacl设置文件权限；`setfacl -m u:user1:rw  1.txt`; `setfacl -m u:user2:rwx 1.txt`
       2. getfacl查看文件权限；`getfacl 1.txt`
       3. 删除文件权限；`setfacl -x user:user1 1.txt`;
       4. 清空文件权限; `setfacl -b 1.txt`
       5.  创建和删除文件；
          -   需要对目录设置acl权限即可
          `setfacl -m u:user4:rwx /ldy`
        6. 如何对目录以及子目录和文件设置 acl权限：加递归。
             `setfacl -m u:user4:rwx  -R  /mnt/` 对存在的文件和目录设置权限
        7. 目录中后期添加的子目录和文件如何继承父目录的权限
              `setfacl -m d:u:user4:rwx -R /mnt/`
    -  sudo权限
        1. visudo:`user1 localhost=/usr/sbin/useradd, /usr/sbin/userdel `
        2. 使用sudo命令；`sudo useradd user1`
        3. 不需要密码使用sudo 命令：`sudo  ALL=NOPASSWD:/usr/sbin/userdel -r user1`
  + shell 脚本
    - 首行解析器命令:`#!/bin/bash`
    -  执行脚本的方式: `1.bash xxx.sh;2 . ./xxx.sh:`
    -  shell脚本使用：
    - shell脚本
      1. 单引号无法解析变量：
      2. expr 可以进行加减乘除；
      3. echo $[] 进行加减乘除；
      4. echo -n 不换行；
      5.  \033[前景颜色；背景颜色m
      6. \033[0m恢复到系统默认的颜色
      7. 前景:30---37:黑，红，绿，棕，蓝，紫，青，白
      8. 背景:40---47:黑，红，绿，棕，蓝，紫，青，白
      9.   cat /etc/passwd |more 查看文件更多内容
      10.  cat ~/study/linux.md |head 查看文件的前10行
      11.  cat ~/study/linux.md |tail -2  tail -x 查看尾部x行
      12.  0条件为真，1为假；
      13.  -d 表示是否为目录；
      14. -e 表示目录或者文件是否存在；
      15. -f 表示是否为文件；
      16. -r 当前用户是否有权限读取；
      17. -w 当前用户是否有权限写入；
      18. -x 当前用户是否可执行该文件；
      19. -l 是否为符号链接该文件；
      20.  -eq  等于
      21. ne 不等于;
      22. gt 大于;
      23. lt小于；
      24. le 小于或者等于；
      25. ge 大于或等于；
      26.  字符串判断条件:= , != ,-z :字符串为空；
      27. 条件逻辑：if... elif ...else...和case ...in...
          ```
          if [ $sco -lt 60 ]
            then 
              echo 'it is bad'
            elif [ $sco -lt 70 ]
            then
                  echo 'good'
            else 
              echo 'you are very good'	
            fi
          ```
          ```
                week=`date +%w`
                case $week in
                  1)
                    echo 'work'
                    ;;
                  2)
                        echo 'work2'	
                    ;;
                  3) 
                        echo 'work3'

                        ;;
                  *) 
                    echo "$week"
                    ;;
                esac	       
          ```
  -  shell 之语句循环
    -  while 循环
        ```
            num=3
            tot=0
            while [ $num -gt 0 ]
            do 
              tot=$[$tot+$num]
              num=$[$num-1]	
            done
              echo $tot
        ```
    - for 循环 
    ```
    for(( a=0; a<10;a++));
      do
          echo $a
          sleep  1;
      done
    ```
  -  [函数function](./loop.sh):
  ```
        function loop(  ){
          i=$1;
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
        }
        loop 0
  ```
-  [find 命令](./find.sh)
-  [正则表达式](./reg.sh)
-  [linux启动流程](./linux.sh)