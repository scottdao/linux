
#!/bin/bash

# scott-ldy x

# echo 'aaaaa'
# echo 'bbbbbbb'
# echo 'cccccc'

 for((i=0;i<10;i++));
 do
     echo $i
 done

echo 'disk space'

echo
# df -Th # 磁盘空间

echo

# free -m

for i in `ls    /home`
do
    id  -u  $i
done
