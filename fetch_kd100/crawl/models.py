import sys
sys.path.append("..")
import demjson
from pymongo import MongoClient
from config import config

mc = MongoClient(config.get('MONGO_HOST'),config.get('MONGO_PORT'))

def push(user_id, order_id, channel, state=0):
	db = mc.kd_db
	db.order_info.save({'user_id':user_id,'order_id':order_id, 'channel':channel, 'state':state})
	db.close	#
	return 'push new data success'

def multi_push(items):
	for i in items:
		push(*i)

def pop_from_db():
	"""
	Pop: just simple return current order id from mongodb!
	"""
	db = mc.kd_db
	orders = db.order_info.find({"state":0})
	return orders
	
def process_order(order_gen):
	"""
		to make <class 'pymongo.cursor.Cursor'> as python yield!
		but in this generate, only include `order_id`
	"""
	for order in order_gen:
		order_id = order.get('order_id')
		channel = order.get('channel')
		yield order_id,channel

def pop():
	order_gen = pop_from_db()
	order_id_gen = process_order(order_gen)
	return order_id_gen 

def update(data):
	"""
	"""
	db=mc.kd_db
	order_id=data.get('order_id')
	context = data.get('context')
	state = data.get('state')
	db.order_info.update({'order_id':order_id},{'$set':{'context':context,'state':state}})
	return 'save success'

def quick_update(result, order_id):
	update_item = {}
	data = result.get('data', 'default data')
	info = data.get('info','default info')
	state = info.get('state','default state')
	context = info.get('context','default context')
	update_item['order_id']=order_id
	update_item['state']=state
	update_item['context']=context
	update(update_item)
	
if __name__ == '__main__':
	push('123456','22308677667','sf')
	multi_data = (
			('1','22308677667','sf'),
			('2','22308677667','sf'),
			('3','22308677667','sf'),
			('4','22308677667','sf'),
			('5','22308677667','sf')
			)
	multi_push(multi_data)
	print '*'*100
	query_set = pop()
	for i,j in query_set:
		print i,j
