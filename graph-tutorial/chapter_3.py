from graph import Graph

if __name__ == '__main__':
	import sys
	if len(sys.argv) == 1:
		graph = Graph('network.txt')
		A = input('enter node: ')
		N = input('input Nth degree: ')

	elif len(sys.argv) == 3:
		graph = Graph('network.txt')
		A = sys.argv[1]
		N = sys.argv[2]

	else:
		raise

	print(graph.nth_degree_neighbors(A,N))