- nosql
memcached缓存数据库与redies缓存数据库区别
neo4j图形数据库

./mongod  --shutdown 关闭进程
 - 开启 mongo 数据库
  `mongod --dbpath D:\study\github\nodeKnowledge\study\mongodb\db --port 27018`;
- mongod 关闭.`mongod  --shutdown`;
- mongod 配置文件启动：
  1. `logpath=/ldy/mongodb/log/mongodb.log // 日志文件；
        logappend=false 
        dbpath=/ldy/mongodb/data/db // 数据文件；
        fork=true // 后台，开启子父进程；
        rest=true // 是否开启web控制台； 
        `
  -  mongodb之shell脚本
   1. /mongo/bin/mongo:启动mongo，开启shell脚本。
   2. show dbs --- 已有数据库列表
   3. use dbname 切换并创建数据库
   4. db.account.drop() 删除集合
   5. db.dropDatabase() 删除数据库
   6. show collections  已有集合列表
   7. db.account.find() 查询数据
   8. db.account.save({条件})存数据
   - mongodb之工具
   1. 数据库备份：mongodump   -h  dbhost  -d dbname  -o dbdirectory
   2. 查看备份数据库的数据：bsondump 
   `./bsondump  ./dump/ldy/account.bson`
   3. 恢复数据库：mongorestore -h dbhost -d dbname --dbdirectoryperdb  dbdirectory
   4. 数据导出：mongoexport  
   ```
   ./mongoexport -d ldy -c account -q {条件} -f name,add （属性）--type=csv > account.csv
   ```
   5. 数据导入：mongoimport
   ```
    ./mongoimport  -d ldy  -c account  --type csv --headerline --drop< account.csv
   ```

   #### 数据库基本概念
   - 文档，集合:没有模式的表；
   - 文档：多个键值有序存放在一起；单键值文档和多键值文档；区分数据类型，键区分大小写，不允许重复的键；
   -  集合: 一组文档，与sql表类似；集合无模式，有开发者把握；
   1. 集合不能有空字符串；
   2. 集合命名不能含有保留字符$；
   - 数据库：一个mongod实列可以存放多个数据库；全部小写；不能空子符；系统保留数据库，admin,local;
    1. local,永远不会被复制；
    2. config: 内部使用，保存分片信息；
    3.  命名空间不能超过121字节；
#### 基础数据类型
   +  支持js正则表达式
   + 基本数据类型，new Date()；
   +  支持js代码；
    + 支持二进制数据（通过代码写进取），不支持shell写入；
    + 支持js的引用类型；
    + 内嵌文档；
    + bson 二进制，节省空间，支持数据类型比json更多。
    + objectId格式：
       -  12字节 
       - 4位时间戳+3位机器号+2位pid（进程号）+3位计数器
       - 3位计数器共2^24个数； 
##### mongodb增删改
  +  **插入**
      - 插入单个文档：`db.account.insert()`
      -  插入不能超过4MB；批量插入，最大消息不超过16MB。 
      - 插入原理：驱动将文档转为bson，检查是否有id键，传入至数据库，数据库解析bson，不做有效性校验，原样存入数据库。
  + **删除**
      - `db.account.remove()`与`db.account.drop()`区别；
        1. remove不删除索引，性能较差；drop删除这个集合，性能较好；
        2. remove 需要查询条件；drop不需要；
   + **更新**
      - `db.account.update`加条件; $set用法,使用修改器进行局部更新；去掉键值：$unset；$inc:对number类型进行加减，必须是数字；$push,数组修改器；$addToSet, 不重复向数组填值；$pop,数组尾删属性1，数组头删属性-1;。
      - 多文档更新：`db.account.update({},{},flase,true(多文档更新))`
      ```
      db.account.update({_id:"123"},{$set:{password:'123'}})
      ```
      - `db.runCommand({getLastError:1})`：执行getLastError时，驱动程序会等待数据库返回结果；
  #### mongodb 查寻语法
   - 查询所有文档：`db.account.find();`
  - 简单条件查询：`db.account.find({'userName':'bbs0'})`;
  - 多值匹配条件:`db.account.find({name:"", pswd:""})`
   - 返回特定的属性值：`db.account.find({},{add:""(返回指定 的属性,设置1返回，0不返回)})`
        ```
        db.account.find({},{add:1,_id:0})//不返回id，返回add属性；
        ```
  + **复合查询条件**
      - $gt: 表示大于,'>';$gte:表示大于等于，">="
      - $lt:表示小于，'<';$lte:表示小于等于,'<='
      - $ne:表示不等于，'!='
      - $in:查询[]具体数据
      - $nin: 查询不是[]条件的数据
      - $or:或查询[]
      - not:可以用于任何条件之上，表示取非；
        ```
        db.account.find({age:{$lt:20}})
        db.account.find({age:{$in:[18,20]}})// 查询范围18,20两条
        db.account.find({age:{$nin:[18,23]}}) // 查询age不是18，23的两条
        db.account.find({$or:[{name:"test"},{age:18}]}) // name值为test，或者age为18
        ```
  + **高级查询  - null**；
      - 条件值：null，即匹配自身，又匹配不存在
        - 若要查出准确的null值，需要结合$exist
      `db.account.find({fullName:{$in:[null],$exists:true}})`
  + **高级查询 - 正则表达式：js**；
      - 遵寻js的正则表达式
      ```
      db.accountfind({name:/^test/i}) //加前缀性能最佳。
      db.account.find({name:/^[a-z]$/i})
      ```
  + **高级查询-查询数组**
      ```
      db.food.insert({fruit:['apple','banana','peach']})
      db.food.insert({fruit:['apple','banana','watermelon']})
      db.food.insert({fruit:['apple','banana','cherry']})
      ```
      - 单元素匹配`db.food.inster(fruit:'cherry')`
      - 多元素匹配`db.food.find({fruit:{$all:['apple','peach']}})`
      - 数组下标`db.food.find({'fruit.2':'cherry'})`
      - 指定数组长度`db.food.find({fruit:{$size:3}})`
  + **高级查询-内嵌文档**
      - 点查寻`db.docment.find({'nameInfo.name':"ldy"})`
      - 内嵌文档，多个键值匹配，采用$elemMatch数组构成的内嵌文档；
      `db.docuemnt.find({list:{$elemMatch:{atr:"caixia",scr:6}}})`
+  **where 查询**
      - 查询文档两个属性或者以上的值相等
      - 不能用索引，并且文档要从bson转成javascript对象，查询速度非常慢
      -  
      ```
      db.food.find({
        $where:function(){//js语法
              for(var current in this){
                for(var other in this){
                  if(current != other && this[current] == this[other]){
                    return true
                  }
                }
              }
              return false;
        }
      })
      ```
+  **游标**
    -  定义游标，不会立即执行：`var cursor = db.liu.find();`
    -  游标迭代器： `while(cursor.hasNext()){ obj = cursor.next(); }`
      - 执行cursor.hasNext()时，查询发送服务器，执行真正查询，shell会获取前100个或者4M数据（两者较小）返回。
      - 游标一定得关闭：`cursor.close()`;
      - 限制数据结果：`db.liu.find().limit(5)`
      - 跳过匹配文档：`db.liu.skip(5)`
      - 排序:sort 用一个对象作为参数，键值表示，键对应文档键名，值表示排序方向。1是生序，-1是降序。
      `db.liu.find().sort({ldy:1})`
      - 多键复合排序：
      `db.account.find.sort({userName：1，age:-1})`

      - skip跳转分页：`db.liu.find({y:'post'}).limit(20).skip(20).sort({ldy:1})`;
      - 游标原理:
          1. 服务端游标消耗内存及资源，要尽快释放；
          2. 游标遍历完成或者客户端发消息终止释放游标；
          3. 游标在客户端不在作用域，驱动会向服务器发消息销毁游标；
          4. 超时销毁机制，游标即使在客户端作用域内，但10分钟不用，也会自动销毁；
          5. 如果关闭游标超时销毁机制，游标使用完，一定要显示将其关闭，否则会一直消耗服务器资源。
+  **[索引创建](./indexes.js)**
      ```
      for(i = 0;i<10000;i++){
        db.acount.insert({userName:"ldy"+i,age:i%60,createTime:new Date()})
    }
      ```
   -    单键索引：`db.account.ensureIndex({userName:1})`
   -    1--表示升序， -1 ---- 表示降序；
   -  复合索引：
      `db.account.ensureIndex({userName:1,age:-1})`
      `db.account.ensureIndex({userName:1,age:1,createTime:1})`
   -  只有索引前部的查询才会得到优化
   - 索引优化查询的同时，会对增删改查带来额外开销。
   - 查找系统索引:`db.acount.indexes.find()`
  + **唯一索引**
  + (**查询工具**)[https://docs.mongodb.com/manual/reference/explain-results/#queryplanner]
  `db.acount.find({userName:1} ).explain( "executionStats" )`;
  + 索引：强制制定索引；
      - hint可以强制制定索引某一个索引；
      - `db.account.find().hint().explain()`
      - 自然选择最优选项。
    + 索引管理：
    - 索引存储每个数据库的systems.indexs集合中这是一个保留的集合，不能直接对数据进行操作，只能通过ensureIndex和drop
Index来操作。
    -  `db.system.indexes.find()`
    - `db.system.namespaces.find()`
    -  修改索引: `db.account.ensureIndex({userName:-1},{'background':true})`,创建索引时，在后台请求，不阻塞正常请求。
    - 删除索引
    - db.runCommand({dropIndexes:"account", index:"age_-1"})
  + **聚合统计**
  - `count`:`db.acount.count();db.account.count({age:30})`
  - `distinct`:
      1. 指定键的不同值；
      2. `db.runCommand({'distinct':"acount",key:"age"})`;必须指定集合和键名。
      3. 计算distinct后的count:`db.runCommand({'distinct':"acount",key:"age"}).values.length`;
      4. `db.runCommand({'distinct':"acount",key:"age", query:{"age":{$gt:30}}}).values.length`
    - 分组：group
      1.   
    + [**mongodb命令-db.runCommand({})**](http://127.0.0.1:28017/_commands)
      -  修复数据库：{repairDatabase:1}
      - 删除集合:{drop:"collection"}
      - 删除当前数据库:{dropDataBase:1}
      - 删除索引:{dropIndexes:collection, index:name}
      - 查看主从服务器:{isMaster:1}
      - 管理员专用:{listDatabases:1}
      - 重命名:{renameCollection:a,to:b},必须是管理员才能修改。
  #### 参考文档
  - (菜鸟教程)[https://www.runoob.com/mongodb/mongodb-indexing.html]
  - (mongodb文档)(https://docs.mongodb.com/)