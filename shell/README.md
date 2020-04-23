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
    - sudo