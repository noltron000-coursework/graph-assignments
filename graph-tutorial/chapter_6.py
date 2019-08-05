from graph import Graph

if __name__ == '__main__':
	import sys

	if len(sys.argv) == 1:
		graph = Graph('network.txt')
	else:
		graph = Graph()

	print(graph.find_largest_clique())