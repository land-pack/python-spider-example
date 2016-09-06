import json
from tornado import web
from tornado import ioloop
from pymongo import MongoClient
from crawl.models import push, query 
from config import config


class ApiHandler(web.RequestHandler):
	def get(self):
		tmp_list = []
		order_id = self.get_argument('order_id')
		self.write(query(order_id))

	def post(self):
		orders = self.get_argument('orders')
		orders=eval(orders)
		for order in orders:
			user_id = order.get('user_id')
			order_id = order.get('order_id')
			channel = order.get('channel')
			push(user_id, order_id,channel)

		self.write("{'status':'ok'}")



if __name__ == '__main__':
	application = web.Application(handlers=[
			('/api/',ApiHandler),
			],
			debug=True)

	application.listen(config.get('API_PORT'))
	ioloop.IOLoop.instance().start()
