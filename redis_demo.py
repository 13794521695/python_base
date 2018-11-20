import redis
# 创建连接
re = redis.Redis(host='192.168.237.131', port='6379', password='123456')

########### 字符串
#       key            value
# re.set('py_name', '你好')
# b ==>  byte
# print(re.get('py_name').decode('utf8'))    中文的话，需要解码成utf8， 不然会变成乱码。
# print(re.get('py_name'))
# re.mset('s_name', 'which', 'age', 18) # 不行的
# re.mset(s_name='hehe', age=19) # 和原生不同
# print(re.mget('s_name', 'age', 'py_name'))
# re.expire('name', 20)
# print(re.ttl('name'))

# re.set('read_count1', 2)
# re.incr('read_count1')
# print(re.get('read_count1'))

#### 列表
# re.lpush('py_list', 1, 2, 3, 'which')
# print(re.lrange('py_list', 0, -1))


# re.hset('py_hash', 'username', 'which')
# print(re.hget('py_hash', 'username'))
# 不同
# re.hmset('py_hash', {"age":"18", "abc":"qwe"})
# print(re.hmget('py_hash', 'username', 'age', 'abc'))
# print(re.hkeys('py_hash'))

print(re.keys())

# re.sadd('py_set', 1, 2 , 3 ,1 , 5, 5)
# print(re.smembers('py_set'))
# re.spop('py_set')
# print(re.smembers('py_set'))


# re.zadd('py_zset', 'a', 11, 'z', 10, 'zz', 1)
# print(re.zrange('py_zset', 0, -1, withscores=True, score_cast_func=int))
# print(re.zrevrange('py_zset', 0, -1, withscores=True, score_cast_func=int))

# 设置订阅
# p_s = re.pubsub()
# # 订阅频道
# p_s.subscribe('fm915.8')
# while True:
#     # 开始订阅
#     p_s.parse_response()
#
#
# # 发布
# p_l = re.publish('fm915.8', 'hello')