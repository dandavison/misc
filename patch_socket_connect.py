import socket

import mock
import redis
import requests

ORIGINAL_VERSIONS_OF_PATCHED_OBJECTS = {
    'socket.socket.connect': socket.socket.connect,
}

def enable_network_connections():
    return mock.patch.object(
        socket.socket,
        'connect',
        ORIGINAL_VERSIONS_OF_PATCHED_OBJECTS['socket.socket.connect'],
    )


mock_method = mock.Mock(
    side_effect=RuntimeError("Outgoing network connections are disabled")
)

# print requests.get('http://www.theguardian.com')

with mock.patch.object(socket.socket,
                       'connect',
                       mock_method):
    with enable_network_connections():
        print requests.get('https://www.theguardian.com')
        # r = redis.StrictRedis(host='www.theguardian.com', port=6379, db=0)
        # r.set('foo', 'bar')

