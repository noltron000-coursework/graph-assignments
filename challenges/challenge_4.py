def sort_knapsack(items, capacity):
	'''
	"capacity" is a numeric value representing a max weight.
	this capacity will be modified as items are added.
	---
	"storage" is a list (usually a set) of item tuples.
	the tuples inside store an item's name, value, and weight.
	this variable represents all possible items available.
	---
	"knapsack" is a list (usually a set) of item tuples.
	the tuples inside store an item's name, value, and weight.
	this variable represents desireable items to pack up.
	'''
	# storage starts full of items with unknown desireabilities.
	# storage holds undesireable items & starts empty.
	storage = items.copy()
	# knapsack holds desireable items & starts empty.
	knapsack = set()
	# as our knapsack fills up, its capacity will decrease.
	print(pack_decision(storage, knapsack, capacity))

def pack_decision(storage, knapsack, capacity):
	# not sure if these are needed...
	storage = storage.copy()
	knapsack = knapsack.copy()

	# base case - knapsack is full or storage is empty.
	if capacity == 0 or len(storage) == 0:
		return knapsack

	# extract current item
	item = storage.pop()
	# create semantic names
	item_name = item[0]
	item_value = item[1]
	item_weight = item[2]

	if item_weight > capacity:
		# item's weight is too heavy to fit in knapsack.
		return pack_decision(storage, knapsack, capacity)

	else:
		# imagine a reality where the current item is added in.
		new_cap = capacity - item_weight
		new_knapsack = knapsack.copy()
		new_knapsack.add(item)
		new_knapsack = pack_decision(storage, new_knapsack, new_cap)
		# imagine a reality where the current item is left out.
		old_knapsack = pack_decision(storage, knapsack, capacity)

		# calculate total values of both backpacks.
		# its O(n), but can be easily improved with refactor.
		def get_value(backpack):
			result = 0
			for column in (row[1] for row in backpack):
				result += column
			return result
		# use function call to calculate sums.
		old_value = get_value(old_knapsack)
		new_value = get_value(new_knapsack)
		print("CHECK IT")
		print(old_value)
		print(new_value)

		# check which scenario is better.
		if new_value >= old_value:
			# knapsack.add(item)
			# capacity -= item_weight
			return new_knapsack

		elif new_value < old_value:
			return old_knapsack


if __name__ == '__main__':
	# a given capacity of the knapsack
	capacity = 50

	# a list of items w/properties, in no particular order
	# properties are: name, value, weight -- in order.
	items = {
		('boot', 60, 10),
		('tent', 100, 20),
		('water', 120, 30),
		('first aid', 70, 15),
	}

	# # BUG this scenario does not work
	# items = {
	# 	('yesterday\'s trash', 1, 50),
	# 	('silver ingot', 100, 100),
	# 	('bag of gold coins', 98, 50),
	# }
	# sort the knapsack
	sort_knapsack(items, capacity)
