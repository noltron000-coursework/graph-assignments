def sort_backpack(capacity, items):
	'''
	this is a simple way to pick the best items first.
	its a solution that does *not* use dynamic programming.
	a solution is found in O(nlog(n)) time.
	'''
	# the packed set is all the items we know we want to pack.
	packed = set()
	# items are sorted by their value and weight,
	# putting the lightest & most valuable items at the front.
	items = sorted(items, key=lambda val: val[1]/val[2])
	# once sorted, the best ratios are added first.
	for item in items:
		name = item[0]
		weight = item[1]
		value = item[2]
		# if the item can fit, it is added.
		if weight <= capacity:
			capacity -= weight
			packed.add(item)
	# the packed set can be deconstructed later.
	print(packed)
	return packed


if __name__ == '__main__':
	# a given capacity of the backpack
	capacity = 100

	# a list of items w/properties, in no particular order
	# items = {
	# 	('boot', 10, 60),
	# 	('tent', 20, 100),
	# 	('water', 30, 120),
	# 	('first aid', 15, 70),
	# }

	# BUG this scenario does not work
	items = {
		('yesterday\'s trash', 50, 1),
		('silver ingot', 100, 100),
		('bag of gold coins', 50, 98),
	}

	# sort the backpack
	sort_backpack(capacity, items)
