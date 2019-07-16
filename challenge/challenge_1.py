'''
Challenge 1
Implement the Graph ADT with an adjacency list
Implement code to read in a graph from a text file to create an instance of the Graph ADT and use it's methods.
Input: A graph file (can contain a directed or undirected graph with or without weights) python3 challenge_1.py graph_data.txt

G
1,2,3,4
(1,2,10)
(1,4,5)
(2,3,5)
(2,4,7)

Output:

The # vertices in the graph.
The # edges in the graph.
A list of the edges with their weights (if weighted)
# Vertices: 4
# Edges: 4
Edge List:
(1,2,10)
(1,4,5)
(2,3,5)
(2,4,7)
'''
import sys

class GraphADT:
	'''
	'''
	def __init__(self, text_file_path=None):
		'''
		'''
		# check for default parameter
		if not text_file_path:
			 text_file_path = input('enter text file: ')
		file_data = self.read_file(text_file_path)
		self.graph = self.extract(file_data)

	def __repr__(self):
		vertices = len(self.graph['nodes'])
		edge_list = self.extract_edges()
		edge_len = len(edge_list.split('\n'))
		return f'''
# Vertices: {vertices}
# Edges: {edge_len}
Edge List:
{edge_list}'''

	def extract_edges(self):
		final_string =''
		for vertex in self.graph['nodes']:
			i_key = vertex
			i_val = self.graph['nodes'][vertex]
			for neighbor in i_val.edges:
				sub_string = f'({i_key},'
				j_key = neighbor
				j_val = i_val.edges[j_key]
				sub_string += j_key
				if j_val:
					sub_string += f',{j_val})\n'
				else:
					sub_string += f')\n'
				final_string += sub_string
		return final_string

	def read_file(self, text_file_path):
		'''
		'''
		file_data = []
		# read file from the source
		with open(text_file_path, 'r') as file:
			file_data = file.readlines()
		# clean file_data by stripping
		for index, entry in enumerate(file_data):
			file_data[index] = entry.strip()
		return file_data

	def extract(self, file_data):
		'''
		'''
		graph = {}

		# get graph type
		graph_type = ''
		if file_data[0].lower() == 'g':
			graph_type = 'graph'
		elif file_data[0].lower() == 'd':
			graph_type = 'digraph'
		else:
			raise
		graph['type'] = graph_type

		# establish new nodes
		node_dict = {}
		node_list = file_data[1].split(',')
		for node_id in node_list:
			node_dict[str(node_id)] = Vertex(str(node_id))
		graph['nodes'] = node_dict

		# populate nodes with edge data
		edge_list = file_data[2:]
		for index, edge in enumerate(edge_list):
			# ensure edge starts as expected
			assert('(' in edge)
			assert(')' in edge)
			# clean edge
			edge = edge.replace('(','')
			edge = edge.replace(')','')
			edge = edge.split(',')
			# edge has no weight
			if len(edge) == 2:
				# node_id_a/_b are just string ids
				node_id_a = str(edge[0])
				node_id_b = str(edge[1])
				# these are actual node objects
				# print(graph['nodes'])
				node_a = graph['nodes'][node_id_a]
				node_b = graph['nodes'][node_id_b]
				# add edge on both nodes
				node_a.add_edge(node_id_b)
				node_b.add_edge(node_id_a)
			# edge is weighted
			elif len(edge) == 3:
				# node_id_a/_b are just string ids
				node_id_a = str(edge[0])
				node_id_b = str(edge[1])
				weight = int(edge[2])
				# these are actual node objects
				node_a = graph['nodes'][node_id_a]
				node_b = graph['nodes'][node_id_b]
				# add edge on both nodes
				node_a.add_edge(node_id_b, weight)
				node_b.add_edge(node_id_a, weight)
			else:
				# unexpected length
				raise

		return graph

class Vertex:
	'''
	'''
	def __init__(self, node_id):
		self.edges = {}

	def __repr__(self):
		return f'\n  NODE -> {self.edges}\n\n'

	def add_edge(self, node_id, weight = None):
		self.edges[node_id] = weight

if __name__ == '__main__':
	if len(sys.argv) == 1:
		test_graph = GraphADT()
	elif len(sys.argv) == 2:
		test_graph = GraphADT(sys.argv[1])
	else:
		raise
	print(test_graph)
