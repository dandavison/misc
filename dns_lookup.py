#!/usr/bin/env python3
import socket
print(socket.getaddrinfo('sfo1-prd-obslb02.counsyl.com', 'www')[0][4][0])
