#!/usr/bin/env python3
import socket
import sys

if __name__ == '__main__':
    hostname, = sys.argv[1:]
    print(hostname)
    print(socket.getaddrinfo(hostname, 'www')[0][4][0])
