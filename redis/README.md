#####  redis

## CAP 原理：
-  高可用 c
- 强一致性 a
- 可容错性 p

## BASE 三个术语的
- 基本可用
-  软状态
- 最终一致

## 分布式 + 集群简介
-  redis:[remote  dictionary  server]
- 安装
    1. 下载： `wget http://download.redis.io/releases/redis-5.0.5.tar.gz`
    2.  解压:   `tar -zxvf redis-5.0.5.tar.gz`
    3.  安装：`cd redis-5.0.5 && make `
    4.  建立软链接: 进入用户全局目录建立链接`cd /usr/bin`;`ln -s /ldy/redis-5.0.5/src/redis-server`
    5.  启动:`redis-server `
    6.  启动服务，进入子父进程：`cd /ldy/redis  && vim redis.conf`
    7. 编辑conf文件，修改:`daemonize yes`,通过`wq!`,保存；
    8. 启动：`redis-server /ldy/redis/redis.conf`即可；