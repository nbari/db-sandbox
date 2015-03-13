import riak
import time

start_time = time.time()

# Connect to Riak.
client = riak.RiakClient(host='10.15.128.254', protocol='http')

# Choose the bucket
bucket = client.bucket('test')

for key in range(1000):
    print ("Stored data: %s" % bucket.get('%s' % key).data)

elapsed_time = time.time() - start_time

print 'Execution time: %.4f' % (elapsed_time)
