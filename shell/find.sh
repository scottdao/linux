
# !/bin/bash


# find 命令查找文件；


# 1. find . -name '*.txt'

# 2. find . -name '[a-z]'

# 3. find /etc -name 'host'

# 4. find . -prem 755

# 5. find user root

# 6. find / -mtime -5 // 找更改时间在5天以内的文件

# 7. find / -mtime +3 // 更改i时间为3天前的文件

# 8. find / -type d  // 查找文件类型为d的目录文件

# 9. find / -type l //  文件类型为l的链接文件

# 10. find  . -size + 1000000c //查找文件大小为1000000字节的文件

# 11. find  ./test -name '*txt'|xargs rm -rf

