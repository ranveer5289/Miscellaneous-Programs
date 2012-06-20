import urllib
import urllib2
import sys
import re
import subprocess
import shlex

import lxml.html as lh

USERAGENT = 'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20100101 Firefox/12.0'
REFERER = 'http://www.divxstage.eu/player/divxstage.swf'

def build_google_search_url(search_query):

    base_url = "http://www.google.co.in/search?q="
    domain = "site:divxstage.eu"

    search_query = "{0} {1}".format(search_query, domain)
    search_query_encoded = urllib.quote(search_query)

    final_url = "".join([base_url, search_query_encoded])
    print final_url
    return final_url


def custom_google_search(search_url, count):

    headers = {'User-Agent': USERAGENT}

    req = urllib2.Request(search_url, None, headers)
    resp = urllib2.urlopen(req)
    data = resp.read()

    document = lh.fromstring(data)
    divxstage_links_list = document.xpath("//div[5]/div[2]/div/div[4]/div[2]/div[2]/div[2]/div[2]/div/ol/li/div/h3/a/@href")

    if divxstage_links_list:
        filtered_divxstage_links_list = filter(lambda link: "divxstage.eu/video/" in 
                                           link, divxstage_links_list[0:count])

        divxstage_title_list = map(get_title, filtered_divxstage_links_list)
    else:
        print "No url found"
        sys.exit(0)

    return [filtered_divxstage_links_list, divxstage_title_list]

def get_title(link):

    #Get title from the url
    document = lh.parse(link)
    title = document.xpath('//title/text()')
    return "".join(title)

def get_filekey(link):

    document = urllib.urlopen(link)
    content = document.read()

    #Get key parameter from url
    pattern = r'flashvars.filekey="(.*?)";'
    filekey = re.findall(pattern, content)
    
    return "".join(filekey)



def get_download_link(divxstage_url):

    headers = {'User-Agent': USERAGENT, 'Referer': REFERER}

    base_url = 'http://www.divxstage.eu/api/player.api.php'
    
    #Query String parameters
    _pass = "undefined"
    _codes = "1"
    _file =  divxstage_url.split('/')[-1]
    _user = "undefined"
    _key = get_filekey(divxstage_url)

    query_string = {'pass': _pass, 'codes': _codes, 'file': _file, 
                    'user': _user, 'key': _key}

    query_string  = urllib.urlencode(query_string)


    complete_url = "{0}?{1}".format(base_url, query_string)

    content = urllib.urlopen(complete_url).read()

    pattern = r"url=(.*?)&title"
    download_link = re.findall(pattern,content)
    download_link =  "".join(download_link)

    return download_link

def dowload_process(url, count):

    links,titles = custom_google_search(url, count)

    for title in titles:
        print "Title===> ", title

    link_number = input("Enter which link to download....")
    divxstage_link = links[link_number-1]
    title = titles[link_number-1]

    download_link = get_download_link(divxstage_link)

    return [download_link, title]


def download_file_wget(link, filename):
    
    command = 'wget "{0}" -O "{1}.flv"'.format(link, filename)
    command = shlex.split(command)
    command_suspend = 'sudo pm-suspend'
    command_suspend = shlex.split(command_suspend)
    subprocess.call(command)
    subprocess.call(command_suspend)
    sys.exit(0)
