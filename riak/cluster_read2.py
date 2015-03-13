import riak
import time

start_time = time.time()

pool = ['10.15.129.215',
        '10.15.129.216',
        '10.15.129.217',
        '10.15.129.218',
        '10.15.129.219']

client = riak.RiakClient(protocol='pbc', nodes=[
    {'host': pool[0]},
    {'host': pool[1]},
    {'host': pool[2]},
    {'host': pool[3]},
    {'host': pool[4]},
    ])

client = client.bucket('test')


for key in range(1000):
    print 'Stored data for key %d-%s: %s' % (
        key, pool[key % 5], client.get('%d-%s' % (key, pool[key % 5])).data)


elapsed_time = time.time() - start_time

print 'Execution time: %.4f' % (elapsed_time)
