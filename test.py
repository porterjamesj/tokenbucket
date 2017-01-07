from tokenbucket import TokenBucket
from threading import Thread
import logging
logging.basicConfig()


def take_10_tokens(i, bucket):
    log = logging.getLogger(f"thread_{i}")
    log.setLevel(logging.INFO)
    log.info("attempting to take 10 tokens")
    bucket.consume(10)
    log.info("10 tokens taken")


def main():
    bucket = TokenBucket(rate=10)
    threads = [Thread(target=take_10_tokens, args=(i, bucket))
               for i in range(10)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
