
import re
import json
import csv
import sys
import codecs
import urllib
import urllib2
from urllib import urlencode


def shorturl(longurl):
    m = {}
    m["url"]=longurl
    para = urlencode(m)
    url = "http://api.t.sina.com.cn/short_url/shorten.json?source=1681459862&url_long="+para[4:];
    req = urllib2.Request(url)
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    ss = json.loads(res)
    return ss[0]['url_short']

reload(sys)
sys.setdefaultencoding("utf-8")



writer = csv.writer(file('csv-1-20.csv','wb'),delimiter=',',quotechar='"',quoting=csv.QUOTE_NONNUMERIC)

for i in range(1,20):
    print i
    p = bytes(i)
    f = open(p+'.html','r')
    for line in f:
        l = line.strip()
        if (l.startswith('wx.cgiData =')):
            jo = l
    f.close()
    
    jsoncontent = jo[13:-1]
    s = json.loads(jsoncontent)
    for item in s['item']:
        for mitem in item['multi_item']:
            c1 = mitem['title']
            c2 = mitem['cover']
            c3 = mitem['content_url']
	    c4 = 0 
            if (mitem['seq']==0):
	        c4=1
            c5 = mitem['digest']
	    picurl = shorturl(c2)
            url = shorturl(c3)        
            writer.writerow([c1,c5,picurl,c2,c4,url,c3])


