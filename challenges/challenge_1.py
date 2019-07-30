import sys
from graph import Graph

def main(Graph):
	Graph = Graph.graph
	graph_type = Graph['type']
	vert_count = None
	edge_count = None
	edge_list  = None

	# summary is a multi-line output
	summary = '' \
	f'Graph Type: {graph_type}\n' \
	f'# Vertices: {vert_count}\n' \
	f'# Edges: {edge_count}\n' \
	f'Edge List:\n{edge_list}\n'

	print(summary)

if __name__ == '__main__':
	if len(sys.argv) == 1:
		main(Graph())

	elif len(sys.argv) == 2:
		main(Graph(sys.argv[1]))

	else:
		raise