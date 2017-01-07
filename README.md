# tokenbucket

A simple token bucket implementation in Python 3.6.

~~~python
from tokenbucket import TokenBucket

bucket = TokenBucket(
    # fills a 10 tokens per second
    rate=10
    # starts with 100 tokens
    tokens=100
    # maximum capacity of 500 tokens
    capacity=500
)

# consume 300 tokens, blocking until they are available
bucket.consume(300)
~~~

There's a small demo with multiple threads in `test.py`.
