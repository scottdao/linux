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
      - chmod u+x file
    - acl
    - sudo