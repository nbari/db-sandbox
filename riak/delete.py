import riak
import time

start_time = time.time()

# Connect o Riak
client = riak.RiakClient()

# Choose the bucket to store data in.
bucket = client.bucket('test')

for key in range(1000):
    print ("Deleting %s..." % key), bucket.get('%s' % key).delete()

elapsed_time = time.time() - start_time

print 'Execution time: %.4f' % (elapsed_time)
