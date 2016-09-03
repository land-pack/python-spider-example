import sys
sys.path.append('..')

from crawl.spider import SFOrderCheck

sf = SFOrderCheck(__name__)
orders = sf.load_task()

if __name__ == '__main__':
	for order in orders:
		print order
