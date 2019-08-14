import itertools

def prep_order(selected_size, original_menu):
	###XXX###XXX###XXX###XXX###XXX###
	def divide_sandwich(size, menu):
		"""
			Note:
				this function was found in C++ on: https://www.techiedelight.com/rot-cutting/
			Input:
				an array of prices with indexes that correlate to the size of the pieces of wood.
				an integer of the length of the wood to be cut.
			Output:
				a string of the inputs and the resulting max cost that can be made from the length of the wood and the prices.
		"""
		# dont overwrite parameter for upstream functions.
		menu = menu.copy()
		# discover which menu items are still untouched.
		unvisited = set(original_menu) - set(menu)
		# always start with the lowest possible size.
		key = min(unvisited)

		# this implies the first run
		if len(menu) == 0:
			menu[key] = {
				'price': original_menu[key]
			}
			return divide_sandwich(size, menu)

		# lets examine our given menu more closely.
		# check every combination of two or less items.
		# indeed, that includes combinations of a single item.
		combos = set()
		# add single items to combos
		for item in menu:
			# normally, a combination of one single item
			# would be denoted by a single item in a list.
			# our scripts require two items in a list.
			combos.add((item, item))
		# add double items to combos
		combos |= set(itertools.combinations(menu, 2))
		# now we need to filter our combos set.
		# the sum of the pairs must equal our key!
		for pair in list(combos):
			if pair[0] + pair[1] != key:
				combos.remove(pair)

		# check up the best price out of the set.
		best_combo = min(combos, key=lambda k: (
			menu[k[0]]['price'] + menu[k[1]]['price']
		))
		best_price = (0
			+ menu[best_combo[0]]['price']
			+ menu[best_combo[1]]['price']
		)

		# compare the original menu price
		# with the best price from any combo.
		if original_menu[key] > best_price:
			menu[key] = {
				'price': best_price,
				'sizes': best_combo,
			}
		else:
			menu[key] = {
				'price': original_menu[key]
			}


		# check if further recursion is needed.
		if key == size:
			return menu
		else:
			return divide_sandwich(size, menu)

	###XXX###XXX###XXX###XXX###XXX###
	return divide_sandwich(selected_size, {})


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

	print(prep_order(size, menu))