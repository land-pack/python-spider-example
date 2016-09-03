import sys
sys.path.append('..')

from crawl.spider import SFOrderCheck

sample_order = '606721866344'
sf = SFOrderCheck(__name__)
r=sf.query(orders=sample_order)
sf.show()
