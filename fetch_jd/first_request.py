import urllib
import urllib2
import cookielib
import re
import socket
import os
from bs4 import BeautifulSoup


class JDLogin(object):
	"""
	
	"""
	def __init__(self, url, post_data={}):
		self.url = url
		self.post_data = post_data
	
	def fetch_page(self, time_out=20):
		cookiejar = cookielib.CookieJar()
		urlopener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
		
		try_time = 0
		while True:
			if try_time > time_out:
				print 'try many time but failure ...so exit!' 
				break
			try:
				if self.post_data == {}:
					request = urllib2.Request(self.url)
				else:
					request = urllib2.Request(self.url, urllib.urlencode(self.post_data))
				#page = urllib2.urlopen(req).read()
				url = urlopener.open(request)
				try_time += 1
			except socket.error:
				print 'connection failure'
			else:
				break
		return url.read(500000)

	def init_params(self):
		self.uuid=''
		self.machineNet=''
		self.machineCpu=''
		self.machineDisk=''
		self.eid=''
		self.fp=''
		self._t=''
		self.loginType=''
		#self.kPHpQpTyPM=FFEAT #: Both key & value always change!
		self.loginname=os.environ.get('jdusername')
		self.nloginpwd=os.environ.get('jdpassword')
		self.loginpwd=os.environ.get('jdpassword')
		self.chkRememberMe='on'
		self.authcode=''

	def extract_param_from_page(self):
		page = self.fetch_page()
		bs = BeautifulSoup(page,"html.parser")
		self.uuid=bs.find_all("form")[0].find_all("input")[0]["value"]
		self.machineNet=bs.find_all("form")[0].find_all("input")[1]["value"]
		self.machineCpu=bs.find_all("form")[0].find_all("input")[2]["value"]
		self.machineDisk=bs.find_all("form")[0].find_all("input")[3]["value"]
		self.eid=bs.find_all("form")[0].find_all("input")[4]["value"]
		self.fp=bs.find_all("form")[0].find_all("input")[5]["value"]
		self._t=bs.find_all("form")[0].find_all("input")[6]["value"]
		self.loginType=bs.find_all("form")[0].find_all("input")[7]["value"]
		self.clrName=bs.find_all("form")[0].find_all("input")[8]["name"]
		self.clrValue=bs.find_all("form")[0].find_all("input")[8]["value"]
	
##	def remember_me(self):
##		cookie = cookielib.CookieJar()
##		cookieProc = urllib2.HTTPCookieProcessor(cookie)
##		opener = urllib2.build_opener(cookieProc)
##		opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')]
##		urllib2.install_opener(opener)


	def to_json(self):
		data = {
			'uuid':self.uuid,
			'machineNet':self.machineNet,
			'machineCpu':self.machineCpu,
			'machineDisk':self.machineDisk,
			'eid':self.eid,
			'fp':self.fp,
			'_t':self._t,
			'loginType':self.loginType,
			str(self.clrName):str(self.clrValue),
			'loginname':self.loginname,
			'nloginpwd':self.nloginpwd,
			'loginpwd':self.loginpwd,
		}
		return data

	
	def show(self):
		print 'uuid:%s' % self.uuid
		print 'machineNet:%s' % self.machineNet
		print 'machineCpu: %s' % self.machineCpu
		print 'machineDisk: %s' % self.machineDisk 
		print 'eid: %s' % self.eid
		print 'fp: %s' % self.fp
		print '_t: %s' % self._t
		print 'loginType: %s' % self.loginType 
		print 'clrName: %s' % self.clrName 
		print 'clrValue: %s' % self.clrValue 
		print '*'*80
		print 'username:%s' % self.loginname
		print 'password:%s' % self.loginpwd

	def run(self):
		#self.remember_me()
		self.init_params()
		self.extract_param_from_page()
		self.show()

if __name__ == '__main__':
	url = "https://passport.jd.com/uc/login"
	jd = JDLogin(url=url)
	jd.run()
	auth_url = "http://passport.jd.com/uc/loginService"
	data = jd.to_json()
	# ........
	jdlogin = JDLogin(url=auth_url,post_data=data)
	print jdlogin.fetch_page()
	#jdlogin.remember_me()
	
