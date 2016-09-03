import sys
sys.path.append('..')

from crawl.spider import SFOrderCheck

sf = SFOrderCheck(__name__)
orders = sf.load_task()

if __name__ == '__main__':
	order_ids = sf.process_task()
	for order_id in order_ids:
		print order_id
