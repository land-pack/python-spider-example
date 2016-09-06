def list_to_gen(items):
	"""
	It's covert a list to a string!
	Example input:
	{"cookies": [
        {
            "domain": "www.baidu.com",
            "expires": "Thu, 15 Sep 2016 10:07:56 GMT",
            "expiry": 1473934076,
            "httponly": false,
            "name": "BD_UPN",
            "path": "/",
            "secure": false,
            "value": "143354"
        },
        { # ... # },
		{ # ... # },
		]
	}
	Example output:
	BIDUPSID=62A9C003CA00C0FDAAB5B9B4538C34CD; PSTM=1432735271; BAIDUID=8568BA6DA9EA79CD48521A2CCAEEE63C:FG=1; H_PS_PSSID=19638_1435_17757_17001_20857_20733_20837_20718"
	"""
	for item in items:
		value = item.get('value')
		name = item.get('name')
		yield '{0}={1};'.format(name,value)
		
def to_cookies(items):
	cookies_gen = list_to_gen(items)
	cookies_list = [item for item in cookies_gen]
	cookies = ''.join(cookies_list)
	return cookies

if __name__ == '__main__':
	cookies_list = [
		{'name':'frank','value':'123'},
		{'name':'jack','value':'334'},
		{'name':'lask','value':'445'},
		{'name':'python','value':'556'}
		]

	print to_cookies(cookies_list)
