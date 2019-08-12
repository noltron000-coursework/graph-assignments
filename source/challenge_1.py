# python packages
import sys
# internal projects
from graph import Graph

def main(Graph):
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
	# grab variables for our summary.
	graph_type = graph.type
	edge_count = graph.count_edges()
	vert_count = graph.count_vertices()
	edge_list  = graph.textify_edges()

	# summary is a multi-line output.
	summary = '' \
	f'Graph Type: {graph_type}\n' \
	f'# Vertices: {vert_count}\n' \
	f'# Edges: {edge_count}\n' \
	f'Edge List:\n{edge_list}\n'

	# return the summary.
	return summary

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