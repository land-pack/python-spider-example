import requests

sample_order = {
	'user_id':'123456',
	'order_id':'7890',
}

many_order ={'orders': """[
{
	'user_id':'99099',
	'order_id':'606721866344',
	'channel':'sf',
},
{
	'user_id':'78787',
	'order_id':'606721866344',
	'channel':'sf',
},
]"""
}

r = requests.post('http://localhost:9977/api/',data=many_order)

print 'return :',r.text
