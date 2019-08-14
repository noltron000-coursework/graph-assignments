# python packages
import os
import sys
import inspect

# get reference of current directory.
currentdir = os.path.dirname(
	os.path.abspath(
		inspect.getfile(
			inspect.currentframe())))
# get reference of parent directory.
parentdir = os.path.dirname(currentdir)
# pull contents from parent directory into current.
sys.path.insert(0, parentdir) 

if __name__ == '__main__':
	import sys

	if len(sys.argv) == 1:
		graph = Graph('network.txt')
	else:
		graph = Graph()
	# note that this prints EVERY clique in a graph
	print(graph.find_largest_clique())
