import riak
import time
from uuid import uuid4

start_time = time.time()

pool = ['10.15.129.215',
        '10.15.129.216',
        '10.15.129.217',
        '10.15.129.218',
        '10.15.129.219']

# Connect to Riak.
client = []
for ip in pool:
    print ip
    c = riak.RiakClient(host=ip)
    c = c.bucket('test')
    client.append(c)


for key in range(1000):
    print "Deleting %d-%s" % (key, pool[key % 5])
    r = client[key % 5].get('%d-%s' % (key, pool[key % 5])).delete()
    print r.key

elapsed_time = time.time() - start_time

print 'Execution time: %.4f' % (elapsed_time)
