import sys
from graph import Graph

def main(Object):
	graph_type = Object.graph['type']
	edge_count = Object.count_edges()
	vert_count = Object.count_vertices()
	edge_list  = Object.textify_edges()

	# summary is a multi-line output
	summary = '' \
	f'Graph Type: {graph_type}\n' \
	f'# Vertices: {vert_count}\n' \
	f'# Edges: {edge_count}\n' \
	f'Edge List:\n{edge_list}\n'

	# return the summary
	return summary

def __repr__(self):
	vertices = len(self.graph['vertices'])
	edge_list = self.extract_edges()
	edge_len = len(edge_list.split('\n'))

if __name__ == '__main__':
	if len(sys.argv) == 1:
		output = main(Graph())

	elif len(sys.argv) == 2:
		output = main(Graph(sys.argv[1]))

	else:
		raise

	print(output)