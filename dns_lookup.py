#!/usr/bin/env python3
import socket
import sys
from pprint import pprint

if __name__ == "__main__":
    hostname, = sys.argv[1:]
    print(hostname)
    pprint(socket.getaddrinfo(hostname, "www"))
