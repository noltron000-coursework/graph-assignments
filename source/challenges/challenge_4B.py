def prep_order(menu, desired_size, order=None, check=None):
	if order is None:
		# the sandwich order will usually start empty.
		order = {}
	else:
		# an order object is given, in size:count pairs.
		# these items must be included with the final order.
		pass

	if check is None:
		# this is a list of subs that are no longer considered.
		# usually it will start empty unless some are a no-go.
		check = set()
	else:
		pass

	order = pack_order(menu, desired_size, order, check)
	return order

def pack_order(menu, desired_size, order, check):
	# the sandwich order starts empty.
	if order is None:
		order = {}

	print('\nNEW RECURSION')
	print('=============\n')
	print(order)
	print(desired_size)

	# base case - order_size is filled to match sub_size.
	if desired_size == 0:
		print("HOORAY")
		print(order)
		return order

	elif desired_size < 0:
		print("BOOO")
		print(order)
		return order

	def get_order_price(my_order):
		order_price = 0
		for size in my_order:
			count = my_order[size]
			price = menu[size]
			order_price += count * price
		return order_price

	# must iterate through every size in menu...
	for size in menu:
		if size not in check:
			price = menu[size]

			# imagine a reality where this sub size is kept in.
			kept_order = order.copy()
			kept_check = check.copy()
			if kept_order.get(size) is None:
				kept_order[size] = 1
			else:
				kept_order[size] += 1
			kept_size = desired_size - size
			# recursively call and grab price.
			kept_order = pack_order(
				menu, kept_size, kept_order, kept_check)
			kept_price = get_order_price(kept_order)

			# imagine a reality where this sub size is left out.
			left_order = order.copy()
			left_check = check.copy()
			left_check.add(size)
			left_size = desired_size
			# recursively call and grab price.
			left_order = pack_order(
				menu, left_size, left_order, left_check)
			left_price = get_order_price(left_order)
			
			# decide which order to keep, left or kept.
			if left_price <= kept_price or kept_size < 0:
				# recursively call function
				return left_order

			elif left_price > kept_price:
				# recursively call function
				return kept_order
			else:
				raise
		else:
			pass
	else:
		raise
	

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
	size = 12

	print(prep_order(menu, size))