from redis import Redis

redis = Redis(host="localhost", port=6379, db=0)


def set_keys(n):
    for i in range(n):
        redis.set(i, i)


def scan_keys(count):
    cursor = 0
    keys = []
    while True:
        cursor, key_chunk = redis.scan(cursor=cursor, count=count)
        keys.append(key_chunk)
        if cursor == 0:
            break

    total = sum(len(chunk) for chunk in keys)
    print(f"Returned {total} keys")

    return keys
