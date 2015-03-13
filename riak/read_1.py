import riak
import time

start_time = time.time()

# Connect to Riak.
client = riak.RiakClient(host='10.15.129.215')

# Choose the bucket
bucket = client.bucket('test')

key = '999-4'

print "Stored data: %s" % bucket.get(key).data

elapsed_time = time.time() - start_time

print 'Execution time: %.4f' % (elapsed_time)
