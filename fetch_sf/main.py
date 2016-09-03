from crawl.spider import SFOrderCheck


sfo = SFOrderCheck(__name__)
#sfo.config.from_object(config='default')



if __name__ == '__main__':
	sfo.run(debug=True,interval=30)
