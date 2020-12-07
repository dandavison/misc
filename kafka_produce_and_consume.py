import os
import socket
from threading import Thread

SERVERS = [s.strip() for s in os.environ["KAFKA_SERVERS"].split()]

def check_connection(server):
    sock = socket.socket()
    host, port = server.split(":")
    return sock.connect((host, int(port)))


print("Checking connections to servers...", end="")
for server in SERVERS:
    check_connection(server)
print("OK")

config = dict(bootstrap_servers=SERVERS,
              security_protocol="SSL")

def consume(topic):
    print(f"consume: topic={topic}")
    from kafka import KafkaConsumer
    consumer = KafkaConsumer(**config)
    consumer.subscribe(topic)
    def consume_loop():
        while True:
            print(next(consumer))
    Thread(target=consume_loop).start()


def produce(topic, msg):
    print(f"produce: topic={topic} msg='{msg}'")
    from kafka import KafkaProducer
    producer = KafkaProducer(**config)
    fut = producer.send(topic=topic, value=msg.encode("utf-8"))
    return fut


if __name__ == '__main__':
    import sys
    topic = sys.argv[1]
    if len(sys.argv) > 2:
        msg, = sys.argv[2:]
        produce(topic, msg)
    else:
        consume(topic)
