def sort_backpack(capacity, items):
	'''
	this is a simple way to pick the best items first.
	its a solution that does *not* use dynamic programming.
	---
	awkwardly enough, this problem has been encountered
	in a certain video game called skyrim.
	incidently, gems have the best value:weight ratio!
	'''
	# the packed set is all the items we want to pack
	packed = set()
	# items are sorted by their value and weight
	items = sorted(items, key=lambda val: val[2]/val[1])
	items.reverse()
	# once sorted, the best ratios are added first.
	for item in items:
		name = item[0]
		weight = item[1]
		value = item[2]
		# if the item can fit, it is added.
		if weight <= capacity:
			capacity -= weight
			packed.add(item)
	# the packed set can be deconstructed later
	print(packed)
	return packed


if __name__ == '__main__':
	capacity = 50
	items = {
		('boot', 10, 60),
		('tent', 20, 100),
		('water', 30, 120),
		('first aid', 15, 70),
	}

	sort_backpack(capacity, items)
