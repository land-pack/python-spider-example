import json
from tornado import web
from tornado import ioloop
from pymongo import MongoClient

mc  = MongoClient('localhost',27017)
db = mc.sf_db



class ApiHandler(web.RequestHandler):
	def get(self):
		tmp_list = []
		order_id = self.get_argument('order_id')
		result = db.order_info.find({'order_id':order_id})
		if result is not None:
			tmp_list = [c for c in result]
			self.write(str(tmp_list))
		else:
			self.write(str({}))

	def post(self):
		orders = self.get_argument('orders')
		orders=eval(orders)
		for order in orders:
			user_id = order.get('user_id')
			order_id = order.get('order_id')
			channel = order.get('channel')
			db.order_info.save({'user_id':user_id,'order_id':order_id,'finish':0,'channel':channel})
		self.write("{'status':'ok'}")



if __name__ == '__main__':
	application = web.Application(handlers=[
			('/api/',ApiHandler),
			],
			debug=True)

	application.listen(9977)
	ioloop.IOLoop.instance().start()
