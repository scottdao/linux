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
  1. 