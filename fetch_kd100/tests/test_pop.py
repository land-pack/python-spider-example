import sys
sys.path.append("..")
from crawl.models import pop


if __name__ == '__main__':
	result = pop()
	for i in result:
		print i
