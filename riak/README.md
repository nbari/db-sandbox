Tutorial
--------

https://github.com/basho/riak-python-client/wiki/Tutorial-%28old%29


To read:

    curl http://10.15.129.219:8098/types/default/buckets/test/key


To write:

    curl -XPUT http://10.15.129.219:8098/buckets/images/keys/FreeBSD.jpg -H 'Content-Type: image/jpeg' --data-binary @FreeBSD.jpg
