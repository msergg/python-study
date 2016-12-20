# CAP theorem

import redis


redis_url = "10.1.14.25"

r = redis.StrictRedis(redis_url)

r.set('a', 1)
r.get('a')

r.lpush('l', 4)
r.lpush('l', 4)

r.lpush('l', 4)

r.lrange('l', 0, -1)

import pymongo

mongo = pymongo.MongoClient(redis_url)
#
# print mongo.database_names()
mongo.get_database('local').get_collection('startup_log').find()

# https://download.robomongo.org/0.9.0/linux/robomongo-0.9.0-linux-x86_64-0786489.tar.gz





# mongo.test.users.insert({'a':1,'b':2})
cursor = mongo.test.users.find()



for i in cursor:
    print i






import elasticsearch
url = "10.1.15.47"

e = elasticsearch.Elasticsearch(url)


# doc = {'name': 'Product1', 'price': 1234 }
#
#
#
# e.index(index='smartyn', doc_type='product', id=1, body=doc)




e.get(index="lifecell-2016.07.26", doc_type='product',id=1)


e.search(index="lifecell-2016.07.26", body={'query': {'match_all': {}}})
