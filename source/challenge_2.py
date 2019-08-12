# python packages
import sys
# internal projects
from graph import Graph

def main(Object, A, B):
	'''
	CHALLENGE 2
	-----------
	this function parses a graph from a special text file.
	next, it finds the shortest path in this graph.
	once this is done, a textual summary is returned.
	the summary includes a few points:
	- the vertices in a shortest path from start to finish.
	- the number of edges in that path.
	'''
	# grab variables for our summary.
	shortest_path = Object.shortest_path_bfs(A,B)
	shortest_edges = len(shortest_path)
	shortest_path = ','.join(shortest_path)

	# summary is a multi-line output.
	summary = '' \
	f'Vertices in shortest path: {shortest_path}\n' \
	f'Number of edges in shortest path: {shortest_edges}\n'

	# return the summary.
	return summary

if __name__ == '__main__':
	# no arguments included!
	if len(sys.argv) == 1:
		start = input('input 1st node: ')
		finish = input('input 2nd node: ')
		output = main(Graph(), start, finish)
	# assume a file is included.
	elif len(sys.argv) == 2:
		file = sys.argv[1]
		start = input('input 1st node: ')
		finish = input('input 2nd node: ')
		output = main(Graph(file), start, finish)
	# assume a start and finish is included.
	elif len(sys.argv) == 3:
		start = sys.argv[1]
		finish = sys.argv[2]
		output = main(Graph(), start, finish)
	# looks like we got everything!
	elif len(sys.argv) == 4:
		file = sys.argv[1]
		start = sys.argv[2]
		finish = sys.argv[3]
		output = main(Graph(file), start, finish)
	# there was a problem D:
	else:
		raise ValueError(
			'too many arguments...'
			f'\n{sys.argv[1:]}'
		)

	# print output to terminal.
	print(output)