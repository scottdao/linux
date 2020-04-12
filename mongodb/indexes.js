/***
 * 
 * 索引创建；
 * 
 * **/

for(i = 0;i<10000;i++){
    db.acount.insert({userName:"ldy"+i,age:i%60,createTime:new Date()})
}
``