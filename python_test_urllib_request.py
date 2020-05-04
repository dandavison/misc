from six.moves.urllib.parse import urlencode
from six.moves.urllib.request import Request
from six.moves.urllib.request import urlopen

url = 'https://enwz9wfrai4cl.x.pipedream.net/'
params = {
    'param_key': 'param_val',
}
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
}
post_body = urlencode(params, doseq=True).encode('utf-8')
req = Request(url, post_body, headers)
post_response = urlopen(req)
