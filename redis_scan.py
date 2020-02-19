import sys

from redis import Redis

redis = Redis(host="localhost", port=6379, db=0)


def set_keys(n):
    for i in range(n):
        redis.set(i, i)


def scan_keys(cursor, count):
    cursor, keys = redis.scan(cursor=cursor, count=count)
    print(f"Returned {len(keys)}, cursor={cursor}")
    return cursor


if __name__ == "__main__":
    n_keys = len(redis.keys("*"))
    print("Number of keys is {n_keys}")
    [cursor, count] = map(int, sys.argv[1:])
    print(scan_keys(cursor, count))
