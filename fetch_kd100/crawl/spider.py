#coding:utf-8

import subprocess
import ujson
import requests
import os
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from utils import to_cookies

cwd = os.getcwd()
js_path = '/home/frank/500.com/kd100/crawl/js'
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def get_baidu_header():
	cmd = "phantomjs " + js_path + "/get_baidu_key.js"

	while True:
		stdout, stderr = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE).communicate()
		try:
			params = ujson.loads(stdout)
			cb = params.get("cb")
			_time = params.get("_")
			cookies = params.get("cookies")
			break
		except ValueError,e:
		#: if javascript run failure, will keep try ...
			print 'try again ...'
			print e

	cookies_str = to_cookies(cookies)
	return {"cb":cb,"timestamp":_time,'cookies':cookies_str}


def check_logistics_info(cb, timestamp,cookies, nu, com):
	"""
	cb callback param from baidu server
	timestamp: a timestamp from baidu server
	nu: order id
	com: logistics company ..
	"""
	url = """https://sp0.baidu.com/9_Q4sjW91Qh3otqbppnN2DJv/pae/channel/data/asyncqury?cb={cb}&appid=4001&com={com}&nu={nu}&vcode=&token=&_={timestamp}"""
	headers = {	'Content-Type': 'application/json;charset=UTF-8',
				'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:48.0) Gecko/20100101 Firefox/48.0',
				'Host':'sp0.baidu.com',
				'Accept':"*/*",
				'Accept-Language':"en-US,en;q=0.5",
				'Accept-Encoding':"gzip,deflate,br",
				'Cookie':cookies,
		}
	url = url.format(cb=cb, nu=nu, timestamp=timestamp, com=com)
	req = requests.get(url, headers=headers, verify=False)
	if req.status_code == 200:
		try:
			ret = req.content.split("(")[1][:-1]
			return ujson.loads(ret)
		except:
			ret = req.content.split("({")[1].split('}]')[0]
			ret = '{'+ret+'}]}}}'
			ret = ujson.loads(ret)
			return ret
	else:
		return {"status":"failure"}

def get_logistics(order_id, channel):
	baidu_session = get_baidu_header()
	cb = baidu_session.get("cb")
	timestamp = baidu_session.get("timestamp")
	cookies = baidu_session.get("cookies")
	return check_logistics_info(cb,timestamp,cookies,order_id, channel)


if __name__ == "__main__":
	nu = "22308677667"
	com = "jd"
	info = get_logistics(nu,com)
	print '*'*100
	print info.get('data')
