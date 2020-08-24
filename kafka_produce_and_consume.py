import os
import socket
from threading import Thread

SERVERS = [s.strip() for s in os.environ["KAFKA_SERVERS"].split()]
TOPIC = "dan-temp-topic"

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

# Consumer
from kafka import KafkaConsumer
consumer = KafkaConsumer(**config)
consumer.subscribe(TOPIC)
Thread(target=lambda: print(next(consumer))).start()


# Producer
from kafka import KafkaProducer
producer = KafkaProducer(**config)
fut = producer.send(topic=TOPIC, value=b"dan-message=1")
