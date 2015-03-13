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

key = '998-3'

print 'Stored data for key %s: %s' % (key, client[3].get(key).data)


elapsed_time = time.time() - start_time

print 'Execution time: %.4f' % (elapsed_time)
