from graph import Graph

if __name__ == '__main__':
	import sys
	if len(sys.argv) == 1:
		graph = Graph('network.txt')
		A = input('enter starting node: ')
		B = input('enter ending node: ')

	elif len(sys.argv) == 3:
		graph = Graph('network.txt')
		A = sys.argv[1]
		B = sys.argv[2]

	else:
		raise

	print(graph.shortest_path_bfs(A,B))