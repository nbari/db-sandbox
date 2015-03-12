import riak
import time
from uuid import uuid4

start_time = time.time()

# Connect to Riak.
client = riak.RiakClient(host='10.15.129.218')

# Choose the bucket to store data in.
bucket = client.bucket('test')

for key in range(1000):
    bucket.new('%s' % key, data={
               'uuid': str(uuid4()),
               'time': time.time()
               }).store()
    print ("Storing key %d" % key)

elapsed_time = time.time() - start_time

print 'Execution time: %.4f' % (elapsed_time)
