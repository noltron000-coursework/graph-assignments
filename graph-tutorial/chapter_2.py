from graph import Graph

if __name__ == '__main__':
	import sys
	if len(sys.argv) == 1:
		graph = Graph('network.txt')
		A = input('enter node: ')
		
	elif len(sys.argv) == 2:
		graph = Graph('network.txt')
		A = sys.argv[1]

	else:
		raise

	print(graph.graph['vertices'][A])