# python packages
import sys
# internal projects
from graph import Graph



def main(Object):
	# grab variables for our summary
	graph_type = Object.type
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



if __name__ == '__main__':
	# no filepath -- ask for a string
	if len(sys.argv) == 1:
		output = main(Graph())

	# looks like we got a filepath!
	elif len(sys.argv) == 2:
		output = main(Graph(sys.argv[1]))

	# there was a problem D:
	else:
		raise

	print(output)