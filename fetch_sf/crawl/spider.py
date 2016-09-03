import os
import sys
import json
import demjson
import requests
from pymongo import MongoClient
from config import config
from celeryapp import fetch_order_info


mc = MongoClient(config.get('MONGO_HOST'),config.get('MONGO_PORT'))
db = mc.sf_db


class SFOrderCheck(object):
	"""
	Expect orders, example '606721866344'
	"""
	prefix='http://www.sf-express.com/sf-service-web/service/bills/'
	subfix='/routes?app=bill&lang=sc&region=cn&translate='
	
	def __init__(self,name,*args,**kwargs):
		self.max_length = config.get('MAX_QUERY',4)
		self.url_prefix = config.get('URL_PREFIX')
		self.url_subfix = config.get('URL_SUBFIX')

	def load_task(self):
		"""
		Read order from rabbitmq/mongodb at intervals throughout;
		{'sf_id':'606721866344','user_id':'12345'}
		`0` is unfinish flag!
		"""
		self.orders = db.order_info.find({'finish':0})	
		return self.orders

	def process_task(self):
		"""
			to make <class 'pymongo.cursor.Cursor'> as python yield!
			but in this generate, only include `order_id`
		"""
		for order in self.orders:
			order_id = order.get('order_id')
			yield order_id
		
	
	def query(self, debug=False):
		"""
			query_set is query set,to check multi-order each time!
			Example: `query_set='1234,5678,9012,3456'`
		"""
		all_order_gen = self.process_task()
		i = 0
		query_set = ''
		for order_id  in all_order_gen:
			if i < self.max_length:
				query_set += str(order_id)+','
				i+=1
			else:
				query_set = self.remove_last_char(query_set)
				self.execute_query(debug=debug,query_set=query_set)
				#: query_set reset to empty!
				query_set=''
				#: i reset to `0`!
				i = 0
		query_set = self.remove_last_char(query_set)
		self.execute_query(debug=debug,query_set=query_set)



	def execute_query(self, debug, query_set):
		if debug == False:
			#: submit run as async mode!
			fetch_order_info.delay(query_set,self.prefix,self.subfix)
			print 'A new task had been send to celery!'
		else:
			print 'Current query set'
			print '*'*80
			print query_set
			print '*'*80

	def remove_last_char(self, old_str):
		str_list = list(old_str)
		str_list.pop()
		return "".join(str_list)

	def run(self,debug=False, interval=30):
		self.load_task()
		self.query()
