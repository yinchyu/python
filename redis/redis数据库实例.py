import redis
pool= redis.ConnectionPool(host="127.0.0.1",port= 6379)
# ,password='helloworld'
r = redis.Redis(connection_pool=pool)

# 普通的string 放入数据库
r.set('foo','bar',nx=True)#设置过期的时间 ,ex=3, 表示经过3秒过期， px =3 表示经过3 毫秒过期
print(r.get('foo').decode('utf8'))

# list数据放入，双向的list

r.lpush("list1", 11, 22, 33)
r.rpush("list1",55,66,77)
r.rpushx("list1",88)
# rpushx 表示向已有的key 中添加元素， 从右添加
print(r.llen("list1"))
r.linsert("list1", "before", "11", "99")   # 往列表中左边第一个出现的元素"11"前插入元素"00"
print(r.lrange("list1", 0, -1))   # 切片取出值，范围是索引号0-最后一个元素
r.lrem("list1",11,0)
print(r.lrange("list1", 0, -1))   # 切片取出值，范围是索引号0-最后一个元素
# num， num=0，删除列表中所有的指定值；
# num=2,从前到后，删除2个； num=1,从前到后，删除左边第1个
# num=-2,从后向前，删除2个

