def prepare_order(menu, desired_size, order=None):
	# the sandwich order starts empty.
	if order is None:
		order = {}
	
	# needed to keep things in check.
	# we dont want to overwrite our current order object.
	order = order.copy()

	# get the total length of the order.
	order_size = 0
	for sub_size in order:
		# order has the number of each item as values.
		order_size = order[sub_size] * sub_size
		# menu has the cost of each item as values.
		order_price = menu[sub_size] * sub_size

	# base case - order_size is filled to match sub_size.
	if order_size == desired_size:
		return order

	# otherwise try to add more subs to the order
	pass



if __name__ == '__main__':
	# create a dictionary of sub sizes with prices.
	menu = {
		1:  0.50,
		2:  1.00, 
		3:  1.69,
		4:  2.00,
		5:  3.00,
		6:  3.49,
		7:  4.50,
		8:  5.25,
		9:  4.00,
		# 10: 6.00, # this shop doesnt always sell this size.
		11: 7.00,
		12: 8.00,
	}

	main(menu, size)