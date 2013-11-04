import redis
import time

start_time = time.time()

# Connect to redis
client = redis.Redis('127.0.0.1', 6379)

for key in range(1000):
    print ("Deleting %s..." % key), client.delete('%s' % key)

elapsed_time = time.time() - start_time

print 'Execution time: %.4f' % (elapsed_time)
