import sys
import urllib2

import json

URL_TO_SHORT = sys.argv[1]

def url_shortener():

    post_url = 'https://www.googleapis.com/urlshortener/v1/url'
    headers = {'Content-Type': 'application/json'}

    data = {'longUrl': URL_TO_SHORT}
    post_data = json.dumps(data)
    
    req = urllib2.Request(post_url, post_data, headers)
    
    try:
        resp = urllib2.urlopen(req)
    
    except urllib2.HTTPError as e:
        print e.code
        print "Request not completed"
        sys.exit(0)
    
    except urllib2.URLError as e:
        print e.reason
        print "Request not completed"
        sys.exit(0)
    
    
    if resp.getcode() == 200:
    
        content = json.loads(resp.read())
    
    else:
    
        pass
    
    tiny_url = str(content['id'])
    return tiny_url


tiny_url = url_shortener()
print tiny_url
