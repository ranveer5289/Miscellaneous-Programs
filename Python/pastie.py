###########################################################
                                                          #
#Usage:                                                   #
# python pastie.py filename                               #      
# python pastie.py -c (To get data from system clipboard) #
                                                          #      
############################################################
import sys
import re
import urllib
import urllib2
import win32clipboard as wc
import win32con


def make_request(url,headers_send,data_send):

    request  = urllib2.Request(url,data_send,headers_send)
    try:
        response = urllib2.urlopen(request)

    except urllib2.HTTPError, e:
        print e.code

    except urllib2.URLError, e:
        print e.reason
        print "Request not completed"
        sys.exit(0)

    page = response.read()
    pattern = r"<title>#(.*?)\s+-\s+Pastie"
    link_id = "".join(re.findall(pattern,page))
    print "http://pastie.org/" + link_id



def read_content_paste(filename):

    with open(filename) as f:
        content = f.read()
    return content

def read_content_clipboard():

    wc.OpenClipboard() 
    clip_data = wc.GetClipboardData(win32con.CF_TEXT) 
    wc.CloseClipboard()
    return clip_data



if "-c" in sys.argv:
    content = read_content_clipboard()
else:
    filename = sys.argv[1]
    content = read_content_paste(filename)



post_url = "http://pastie.org/pastes"
params = {"paste[body]":content,"paste[authorization]":"burger","paste[restricted]":"0","paste[parser_id]":"16"}
data_post = urllib.urlencode(params)
user_agent = "Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20100101 Firefox/12.0"
referer  = "http://pastie.org/"
headers = {"User-Agent":user_agent,"Referer":referer}



make_request(post_url,headers,data_post)
