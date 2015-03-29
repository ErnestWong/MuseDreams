import urllib

url = 'http://localhost:3000/states'

def post_request(state):
    params = urllib.urlencode({
        'state': '{}'.format(state)
    })
    data = urllib.urlopen(url, params).read()

