import sys
import re
sys.path.append("..")
import requests
from celery import Celery
from config import config
from pymongo import MongoClient
import demjson

app = Celery(__file__, broker='amqp://')

def rm_html(old_str):
	dr = re.compile(r'<[^>]+>', re.S)
	dd = dr.sub('', old_str)
	return dd

def filter_field(old_dict):
	new_dict = {}
	new_dict['order_id']=old_dict.get('id')
	new_dict['routes']=old_dict.get('routes')
	return new_dict


@app.task
def fetch_order_info(query_set,prefix,subfix):
		"""
		cause submit communicate to the website, 
		so it's best to run as async mode!
		There are many choise can pick up! `tornado` ,`celery` etc ..
		prefix='http://www.sf-express.com/sf-service-web/service/bills/'
		subfix='/routes?app=bill&lang=sc&region=cn&translate='
		"""
		mc = MongoClient(config.get('MONGO_HOST'),config.get('MONGO_PORT'))
		db = mc.sf_db
		url = prefix+query_set+subfix
		r = requests.get(url)
		data = r.text
		data = rm_html(data)
		data = demjson.decode(data)
		for c in data:
			c = filter_field(c)
#db.order_info.save(c)
			order_id = c.get('order_id')
			routes = c.get('routes')
			db.order_info.update({'order_id':order_id},{'$set':{'routes':routes}})
		return 'finish ...'


