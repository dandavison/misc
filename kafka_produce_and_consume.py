import json
import os
import socket

from kafka import KafkaConsumer
from kafka import KafkaProducer

def check_connection(server):
    sock = socket.socket()
    host, port = server.split(":")
    return sock.connect((host, int(port)))

# E.g.
# export KAFKA_SERVERS='b-2.lims-staging.x7e7yl.c3.kafka.us-west-2.amazonaws.com:9094 b-1.lims-staging.x7e7yl.c3.kafka.us-west-2.amazonaws.com:9094 b-3.lims-staging.x7e7yl.c3.kafka.us-west-2.amazonaws.com:9094' 
SERVERS = [s.strip() for s in os.environ["KAFKA_SERVERS"].split()]

print("Checking connections to servers...", end="")
for server in SERVERS:
    check_connection(server)
print("OK")

config = dict(bootstrap_servers=SERVERS,
              security_protocol="SSL")

producer = KafkaProducer(value_serializer=lambda x: json.dumps(x).encode('utf-8'), **config)
consumer = KafkaConsumer(**config)

print("Producing")
producer.send("dan-temp-topic", "dan-message=1")
print("Consuming")
for i in range(10):
    print(consumer.poll(1000, 1))
