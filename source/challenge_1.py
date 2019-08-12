# python packages
import sys
# internal projects
from graph import Graph

def main(graph):
	'''
	CHALLENGE 1
	-----------
	this function parses a graph from a special text file.
	once this is done, a textual summary is returned.
	the summary includes a few points:
	- the # vertices in the graph.
	- the # edges in the graph.
	- a list of the edges with their weights (if weighted).
	'''

	# return the summary.
	# == NOTE ==
	# __repr__ has been modified to give an expected output.
	return graph

if __name__ == '__main__':
	# no filepath.
	if len(sys.argv) == 1:
		output = main(Graph())
	# looks like we got a filepath!
	elif len(sys.argv) == 2:
		output = main(Graph(sys.argv[1]))
	# there was a problem D:
	else:
		raise ValueError(
			'too many arguments...'
			f'\n{sys.argv[1:]}'
		)

	# print output to terminal.
	print(output)