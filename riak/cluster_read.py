import riak
import time

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
    print 'Stored data for key %d-%s: %s' % (
        key, key % 5, client[key % 5].get('%d-%s' % (key, pool[key % 5])).data)


elapsed_time = time.time() - start_time

print 'Execution time: %.4f' % (elapsed_time)
