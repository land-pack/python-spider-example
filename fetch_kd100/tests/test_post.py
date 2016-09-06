import requests

many_order ={'orders': """[
{
	'user_id':'888888',
	'order_id':'22308677667',
	'channel':'jd',
},
{
	'user_id':'78787',
	'order_id':'606721866344',
	'channel':'shunfeng',
},
]"""
}

r = requests.post('http://localhost:9977/api/',data=many_order)

print 'return :',r.text
