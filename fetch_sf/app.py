import os
import json
import demjson
import requests


sample_order = '606721866344'


class SFOrderCheck(object):
	"""
	Expect orders, example '606721866344'
	"""
	prefix='http://www.sf-express.com/sf-service-web/service/bills/'
	subfix='/routes?app=bill&lang=sc&region=cn&translate='
	
	def __init__(self):
		pass

	def load_task(self):
		"""
		Read order from rabbitmq at intervals throughout;
		{'sf_id':'606721866344','user_id':'12345'}
		"""
		
	
	def query(self, orders=sample_order):
		r = requests.get(self.prefix+orders+self.subfix)
		self.text=r.text
		self.json_data = demjson.decode(self.text)
		self.parsed=json.loads(self.text)
		return r.text

	def show(self):
		parsed = json.loads(self.json_data)
		print json.dumps(parsed,indent=4,sort_keys=True)

	def to_json(self):
		"""
		Cause, we only care about `sf_id`,`user_id`,`routes` field, so I 
		extract those field to save into mongodb!
		"""
		for order in self.json_data:
			sf_id = order.get('id')
			#user_id = order.get(sf_id)
			sf_routes = order.get('routes')
			#print sf_id
			#print sf_routes

	def save(self):
		
		pass			

	

sf = SFOrderCheck()
r = sf.query(orders=sample_order)
#sf.show()
sf.to_json()
