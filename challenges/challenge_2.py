# python packages
import sys
# internal projects
from graph import Graph



def main(Object, A, B):
	# grab variables for our summary
	shortest_path = Object.shortest_path_bfs(A,B)
	shortest_edges = len(shortest_path)
	shortest_path = ','.join(shortest_path)

	# summary is a multi-line output
	summary = '' \
	f'Vertices in shortest path: {shortest_path}\n' \
	f'Number of edges in shortest path: {shortest_edges}\n'

	# return the summary
	return summary



if __name__ == '__main__':
	# no filepath -- ask for a string
	if len(sys.argv) == 3:
		A = sys.argv[1]
		B = sys.argv[2]
		output = main(Graph(), A, B)

	# looks like we got a filepath!
	elif len(sys.argv) == 4:
		A = sys.argv[2]
		B = sys.argv[3]
		output = main(Graph(sys.argv[1]), A, B)

	# there was a problem D:
	else:
		raise

	print(output)