# -XXX-XXX-
# NOTE: this code was pulled from Jamie McCrory's repo.
# check it out here: https://github.com/jamiejamiebobamie/CS-2.2-Advanced-Recursion-and-Graphs/blob/master/challenges/challenge4/part2.py
# -XXX-XXX-

def driver_function(prices,n):
	"""
	The driver holds the lookup dictionary and makes the original function call to rodcut function.
	"""
	dict = {}

	def rodcut(prices,n):
		"""
			Note:
				this function was found in C++ on: https://www.techiedelight.com/rot-cutting/
			Input:
				an array of prices with indexes that correlate to the size of the pieces of wood.
				an integer of the length of the wood to be cut.
			Output:
				a string of the inputs and the resulting max cost that can be made from the length of the wood and the prices.
		"""
		# each time the function gets called initialize maxValue to be negative infinity
		maxValue = float('-inf')

		# return 0 if the input length of the rod is 0 or if the input length is greater than the array as that will throw list index out of range errors below
		if n == 0 or len(prices) <= n:
			return 0

		# generate numbers between 1 and the current rod_length + 1 (+1 because range() is non-inclusive at the upper bounds)
		for _ in range(1, n+1):

			# set 'entry' to a tuple of the current cut. a cut consists of two pieces.
			# cut == piece A and piece B: A is: _ and piece B is: the length of the rod - piece A.
			cut = (_, n-_)

			# memoization dictionary:
			if cut in dict:
				cost = dict[cut]
			else:
			# reference the price for piece A, taking into account the index of piece A will be: _-1
			# need to determine the cost(s) of all pieces resulting from that cut.
			# so piece B is fed into "the wood chipper": the rodCut function, to determine its cost(s)
				cost = prices[_-1] + rodcut(prices, n - _)
				dict[cut] = cost

			# if the resuting cost is greater than the local maxValue set the local maxValue to the cost
			if (cost > maxValue):
				maxValue = cost

		# return the maxValue to the outside scope.
		return maxValue

	maxValue = rodcut(prices,n)
	printable_prices = [str(price) for price in prices]

	return "For this input:\n\n"+ "prices: " + ", ".join(printable_prices) + "\nwood length: " + str(n) + "\n\nThe solution is:\n\n" + str(maxValue)

			

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