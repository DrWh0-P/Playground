import urllib.request as q
import urllib
import re
import json


def follow(url):
    #substituting ? with.json or adding .json depending on the url
    if re.search("\\?",url):
        url=re.sub("\\?",".json?",url)
    else:
        url=url + ".json" 
    try:
        req=q.Request(url)
        #to make sure the server doesnt identify as a bot
        req.add_header("User-Agent","Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11)  Gecko/20071127 Firefox/2.0.0.11")
        data=q.urlopen(req).read().decode()
        data=json.loads(data)
        url=data['follow']
        follow(url)
    except urllib.error.HTTPError as e:
        print (e.fp.read())
    

follow('http://letsrevolutionizetesting.com/challenge')
