import socket
import urllib2

import mock
import requests


ORIGINAL_VERSIONS_OF_PATCHED_OBJECTS = {
    'socket.socket.connect': socket.socket.connect,
}

HOSTS = [
    'http://www.counsyl.com',
    'http://api.twilio.com',
    'http://localhost',
    'http://127.0.0.1',
]


def connect(self, address):
    print '\t\t', address

    real_connect = (
        ORIGINAL_VERSIONS_OF_PATCHED_OBJECTS['socket.socket.connect'])
    return real_connect(self, address)


with mock.patch.object(socket.socket, 'connect', connect):
    for host in HOSTS:
        print
        print host

        for fn, library in [(requests.get, 'requests'),
                            (urllib2.urlopen, 'urllib2')]:
            print
            print '\t', library
            try:
                fn(host)
            except Exception as ex:
                print '\t', '%s(%s)' % (type(ex).__name__, ex)
