import urllib
import urllib2
import cookielib
import re
import socket
import os
from bs4 import BeautifulSoup


def Navigate(url, data={}):
    tryTimes = 0
    while True:
        if (tryTimes > 20):
            print 'try many time ..'
            break
        try:
            if (data == {}):
                req = urllib2.Request(url)
            else:
                req = urllib2.Request(url, urllib.urlencode(data))
            req = urllib2.urlopen(req).read()
            tryTimes = tryTimes + 1
        except socket.error:
            print 'connection failure'
        else:
            break
    return req

def func():
    try:
        cookie = cookielib.CookieJar()
        cookieProc = urllib2.HTTPCookieProcessor(cookie)
    except:
        raise
    else:
        opener = urllib2.build_opener(cookieProc)
        opener.addheaders = [('User-Agent',
                              'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')]
        urllib2.install_opener(opener)

url = "https://passport.jd.com/uc/login"
login = Navigate(url)
loginSoup = BeautifulSoup(login,"html.parser")
# looking for uuid
uuid = loginSoup.find_all("form")[0].find_all("input")[0]['value']
#print uuid
clrName=loginSoup.find_all("form")[0].find_all("input")[6]['name']
clrValue=loginSoup.find_all("form")[0].find_all("input")[6]['value']
# look rand prama..
###clr = loginSoup.find_all("span", "clr")[0]
###clrName = clr.find_next_siblings("input")[0]['name']
###clrValue = clr.find_next_siblings("input")[0]['value']
print clrName,clrValue
###
auth_url = "http://passport.jd.com/uc/loginService"
myurl = 'http://127.0.0.1:5000'
#loginurl = 'https://passport.jd.com/new/misc/js/login2016.js'
# print url

post_data = {
    'loginname': os.environ.get('jdusername') or 'your-username',
    'nloginpwd': os.environ.get('jdpassword') or 'your-password',
    'loginpwd':  os.environ.get('jdpassword') or 'your-password',
##  'machineNet':'',
##    'machineCpu':'',
##  'machineDisk':'', 
    str(clrName):str(clrValue),
    'uuid': uuid,
    'authcode': ''
}
#passport = Navigate(url, postData)
#print passport 


# after verify success ...
cookieJar = cookielib.CookieJar()
# instance a global opener

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
# get cookie
req = urllib2.Request(auth_url, post_data, headers)

###result = opener.open(req)

#### visit home of jd with cookie
result = opener.open('http://i.jd.com/user/info')

# show result
print result.read().decode('gbk').encode('utf8')

#soup = BeautifulSoup(result,'html.parser')

#nickname = soup.find_all("input",id="nickName")[0]['value']

#print "nickname:",nickname 


