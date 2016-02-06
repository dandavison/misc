import json
import requests


HEADERS = {
    'accept': 'application/json',
    'content_type': 'application/json',
}


def get_json(url, **kwargs):
    resp = requests.get(
        url,
        headers=HEADERS,
        **kwargs
    )
    with open('/tmp/resp.html', 'w') as fp:
        fp.write(resp.content)
    print resp.status_code
    return resp


def put(url, data, **kwargs):
    _post_or_put('put', url, data, **kwargs)


def post(url, data, **kwargs):
    _post_or_put('post', url, data, **kwargs)

def _post_or_put(verb, url, data, **kwargs):
    resp = getattr(requests, verb)(
        url,
        data=json.dumps(data),
        headers=HEADERS,
        **kwargs
    )
    with open('/tmp/resp.html', 'w') as fp:
        fp.write(resp.content)
    print resp.status_code
    return resp
