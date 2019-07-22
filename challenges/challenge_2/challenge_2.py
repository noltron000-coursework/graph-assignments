import sys
import re



class Graph:
	''''''
	def __init__(self, filepath=None):
		''''''
		if not filepath:
			filepath = input('input the filepath to a graph: ')
		text_data = self.read_file(filepath)
		self.graph = self.extract(text_data)

	def __repr__(self):
		return str(self.graph)

	def extract(self, text_data):
		''''''
		graph = {}

		# get graph type
		graph_type = ''
		if text_data[0].lower() == 'g':
			graph_type = 'graph'
		elif text_data[0].lower() == 'd':
			graph_type = 'digraph'
		else:
			raise
		graph['type'] = graph_type

		# establish new vertices
		vertex_dict = {}
		vertex_list = text_data[1].split(',')
		for vertex_id in vertex_list:
			vertex_dict[str(vertex_id)] = Vertex(str(vertex_id))
		graph['vertices'] = vertex_dict

		# populate vertices with edge data
		edge_list = text_data[2:]
		for index, edge in enumerate(edge_list):

			# ensure edge starts as expected
			assert('(' in edge)
			assert(')' in edge)
			# clean edge
			edge = re.sub(r'[\(\)]', '', edge)
			edge = edge.split(',')

			# edge has no weight
			if len(edge) == 2:
				# vertex_id_a/_b are just string ids
				vertex_a_id = str(edge[0])
				vertex_b_id = str(edge[1])
				# these are actual vertex objects
				VertexA = graph['vertices'][vertex_a_id]
				VertexB = graph['vertices'][vertex_b_id]
				# add edge on both vertices
				VertexA.add_edge(vertex_b_id)
				VertexB.add_edge(vertex_a_id)

			# edge is weighted
			elif len(edge) == 3:
				# vertex_a_id/_b are just string ids
				vertex_a_id = str(edge[0])
				vertex_b_id = str(edge[1])
				weight = int(edge[2])
				# these are actual vertex objects
				VertexA = graph['vertices'][vertex_a_id]
				VertexB = graph['vertices'][vertex_b_id]
				# add edge on both vertices
				VertexA.add_edge(vertex_b_id, weight)
				VertexB.add_edge(vertex_a_id, weight)

			# unexpected length
			else:
				raise
		return graph

	def read_file(self, text_file_path):
		''''''
		text_data = []
		# read file from the source
		with open(text_file_path, 'r') as file:
			text_data = file.readlines()
		# clean text_data by stripping
		for index, entry in enumerate(text_data):
			text_data[index] = entry.strip()
		return text_data

	def shortest_path_bfs(self, A, B):
		# create hot-vars
		vertices = self.graph['vertices']
		# create visited set, and visit vertex A
		visited = {A}
		# create vertex queue, and start with vertex A
		queue = [A] # HACK not a real queue

		while queue != []:
			# dequeue first vertex
			# HACK change later for non-array
			V = queue.pop()
			print(V)
			# add its neighbors to the queue
			for N in vertices[V].edges:
				if N in visited:
					pass
				else:
					# visit the vertex
					visited.add(N)
					# HACK change later for non-array
					queue.insert(0, N)



class Vertex:
	''''''
	def __init__(self, vertex_id):
		self.edges = {}

	def __repr__(self):
		return f'GRAPH {str(self.edges)}'

	def add_edge(self, vertex_id, weight=None):
		self.edges[vertex_id] = weight



if __name__ == '__main__':
	if len(sys.argv) == 1:
		test_graph = Graph()
	elif len(sys.argv) == 2:
		test_graph = Graph(sys.argv[1])
	else:
		raise
	# print(test_graph)
	test_graph.shortest_path_bfs('1','5')