from crawl.spider import get_logistics_info
from crawl.models import pop, quick_update


def main():
	order_gens = pop()
	for order_gen in order_gens:
		update_item = {}
		order_id , channel = order_gen
		result = get_logistics_info(order_id, channel)
		quick_update(result,order_id)



if __name__ == '__main__':
	main()
