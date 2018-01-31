#!/usr/bin/env python3

class Proxy:
    def __new__(cls, proxied):
        if isinstance(proxied, dict):
            return DictProxy.__new__(proxied)
        elif isinstance (proxied, int):
            return IntProxy.__new__(proxied)
        else:
            raise TypeError


class DictProxy(Proxy):
    def __init__(self, proxied):
        self.proxied = proxied


class IntProxy(Proxy):
    def __init__(self, proxied):
        self.proxied = proxied



dp = Proxy({})
print(dp.__class__)

ip = Proxy(1)
print(ip.__class__)
