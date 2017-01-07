from hypothesis import given
from hypothesis import strategies as st

from threading import Thread
import time

from tokenbucket import TokenBucket


@given(
    requests=st.lists(st.floats(min_value=0, max_value=1),
                      min_size=1, max_size=20),
    rate_limit=st.floats(min_value=10, max_value=50)
)
def test_rate_limiting(requests, rate_limit):
    bucket = TokenBucket(rate=rate_limit, capacity=float('inf'))
    start = bucket._time
    # construct a thread per request
    threads = [Thread(target=lambda b, r=r: b.consume(r), args=(bucket,))
               for r in requests]
    # TODO stagger when the requests come in?
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    stop = time.monotonic()
    elapsed = stop - start
    actual_rate = sum(requests) / elapsed
    assert bucket._tokens > 0
    assert actual_rate < rate_limit
