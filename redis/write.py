import redis
import json
import time
from uuid import uuid4

start_time = time.time()

# Connect to redis
client = redis.Redis('127.0.0.1', 6379)

for key in range(1000):
    client.set(key, {
               'uuid': str(uuid4()),
               'time': time.time()
               })
    print ("Storing key %d" % key)

elapsed_time = time.time() - start_time

print 'Execution time: %.4f' % (elapsed_time)
