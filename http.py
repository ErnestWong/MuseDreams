import urllib

url = 'https://shielded-sierra-1551.herokuapp.com/states.json'
local_url = 'http://localhost:3000/states.json'

def post_request(state):
    params = urllib.urlencode({
        'state': '{}'.format(state)
    })
    try:
        data = urllib.urlopen(url, params).read()
    except: 
        print "error"
