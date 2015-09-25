Tutorial
--------

https://github.com/basho/riak-python-client/wiki/Tutorial-%28old%29

Riak Python Client:

    pip install --user riak


List all keys:

    http://riak.server.tld/buckets/bucket_name/keys?keys=true


example:

    http://riak.server.tld/buckets/test/keys/8


To read:

    curl http://10.15.129.218:8098/types/default/buckets/test/keys/996-10.15.129.216

To write:

    curl -XPUT http://10.15.129.219:8098/buckets/images/keys/FreeBSD.jpg -H 'Content-Type: image/jpeg' --data-binary @FreeBSD.jpg

To read using auth example:

    curl -u riakuser:password https://10.15.129.218:8098/types/default/buckets/test/keys/996-10.15.129.216 --insecure
