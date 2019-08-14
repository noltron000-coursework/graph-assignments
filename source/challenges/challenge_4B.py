import itertools

def prep_order(selected_size, original_menu):
	def divide_sandwich(menu):
		'''
		input:
		the size of the desired sub, and the menu
			an array of prices with indexes that correlate to the size of the pieces of wood.
		an integer of the length of the wood to be cut.
			Output:
				a string of the inputs and the resulting max cost that can be made from the length of the wood and the prices.
		== NOTE ==
		this function was inspired by Jamie McCrory's code.
		'''
		# discover which menu items are still untouched.
		unvisited = set(original_menu) - set(menu)
		# always start with the lowest possible size.
		key = min(unvisited)

		# this implies the first run
		if len(menu) == 0:
			menu[key] = {
				'price': original_menu[key]
			}
			return divide_sandwich(menu)

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

		# == FIXME ==
		# this code works but is pretty ugly.
		# without it, larger items must reference smaller items.
		# for example, if a size 6 was great because it was
		# made up of  three twos, it now adds three twos
		# instead of one six with this code.
		best_sizes = {}
		for good_size in best_combo:
			if menu.get(good_size, {}).get('sizes'):
				for best_size in menu[good_size]['sizes']:
					count = menu[good_size]['sizes'][best_size]
					if best_size in best_sizes:
						best_sizes[best_size] += count
					else:
						best_sizes[best_size] = count
			elif best_sizes.get(good_size):
				best_sizes[good_size] += 1
			else:
				best_sizes[good_size] = 1

		# compare the original menu price
		# with the best price from any combo.
		if original_menu[key] >= best_price:
			menu[key] = {
				'price': best_price,
				'sizes': best_sizes,
			}
		else:
			menu[key] = {
				'price': original_menu[key]
			}

		# check if further recursion is needed.
		if key == selected_size:
			return menu
		else:
			return divide_sandwich(menu)

	###############################
	### RESUME TO MAIN FUNCTION ###
	###############################

	return divide_sandwich({})


if __name__ == '__main__':
	# create a dictionary of sub sizes with prices.
	menu = {
		1:  0.50,
		2:  0.99, 
		3:  1.69,
		4:  2.00,
		5:  3.00,
		6:  3.49,
		7:  4.50,
		8:  5.25,
		9:  4.00,
		10: 6.00,
		11: 7.00,
		12: 8.00,
		13: 8.42,
		14: 9.38,
		15: 19.99,
		16: 14.00,
	}

	size = input(
		'enter a sandwich size between 16" and 1", inclusive...'
		'\n(hint: you can hit just enter for 12")\n\t>>> '
	)
	try:
		size = int(size)
		if 0 > size or size > 16:
			raise
	except:
		print('NOTE: sub size defaulted to 12')
		size = 12

	# grab the result!!!
	result = prep_order(size, menu)[size]

	# create some terminal text
	terminal_text = '---\n' \
	f'A {size}" sub normally costs ${menu[size]}.\n' \
	f'However, if we purchase smaller subs to match ' \
	'that size...then it could be so much lower!\n' \
	'We can actually get the price down to ' \
	f'${result["price"]} if we buy some smaller subs:\n'
	# add some dynamics to the terminal text
	for size in result['sizes']:
		count = result['sizes'][size]
		terminal_text += f'- {count} {size}" sub(s)\n'
	f'{result["sizes"]}'
	
	print(terminal_text)