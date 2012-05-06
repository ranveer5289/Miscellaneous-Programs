#Ranveer Raghuwanshi
import urllib
import os
import urllib2
import hashlib
import sys
from urllib2 import URLError

filename = sys.argv[1]
print filename



def get_hash(name):
        readsize = 64 * 1024
        with open(name, 'rb') as f:
            size = os.path.getsize(name)
            data = f.read(readsize)
            f.seek(-readsize, os.SEEK_END)
            data += f.read(readsize)
            print hashlib.md5(data).hexdigest()
        return hashlib.md5(data).hexdigest()
            

def download_srt(filehash):
        parameters = {'action' : 'download', 'hash' : filehash,'language' : 'en'}
        user_agent = 'SubDB/1.0 (download_srt/0.1; https://github.com/ranveer5289)'

        encoded_url = urllib.urlencode(parameters)
        final_url = "http://api.thesubdb.com/?" + encoded_url

        req_object = urllib2.Request(final_url)
        req_object.add_header('User-Agent', user_agent)

        try:
                 page_content = urllib2.urlopen(req_object)

        except URLError, e:
                if e.code == 404:
                        print "Subtitle not found"
                        sys.exit(0)
      
        content_srt = page_content.read()
        return content_srt


def create_srt_file(content):
        srt_name = filename[:-3] + "srt"
        f = open(srt_name, "w")
        f.write(content)
        f.close()





filehash = get_hash(filename)
content = download_srt(filehash)
create_srt_file(content)
