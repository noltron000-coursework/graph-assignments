# python packages
from vertex import Vertex
# internal projects
import sys
import re



class Graph:
	'''
	'''


	def __init__(self, filepath=None):
		'''
		'''
		if not filepath:
			filepath = input('input the filepath to a graph: ')
		text_data = self.read_file(filepath)
		self.graph = self.extract(text_data)


	def __repr__(self):
		return str(self.graph)


	def read_file(self, text_file_path):
		'''
		'''
		text_data = []
		# read file from the source
		with open(text_file_path, 'r') as file:
			text_data = file.readlines()
		# clean text_data by stripping
		for index, entry in enumerate(text_data):
			text_data[index] = entry.strip()
		return text_data


	def extract(self, text_data):
		'''
		'''
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
		# loop through every edge
		for index, edge in enumerate(edge_list):
			# ensure edge starts as expected
			assert('(' in edge)
			assert(')' in edge)
			# clean edge
			edge = re.sub(r'[\(\)]', '', edge)
			edge = edge.split(',')
			# vertex_a_id/_b_id are just string ids
			vertex_a_id = str(edge[0])
			vertex_b_id = str(edge[1])
			# these are actual vertex objects
			VertexA = graph['vertices'][vertex_a_id]
			VertexB = graph['vertices'][vertex_b_id]

			# edge has no weight
			if len(edge) == 2:
				# add edge on main vertex
				VertexA.add_edge(vertex_b_id)
				# if this is not a digraph, add an edge back
				if graph['type'] == 'graph':
					VertexB.add_edge(vertex_a_id)

			# edge is weighted
			elif len(edge) == 3:
				# the third item is the weight
				weight = int(edge[2])
				# add edge on both vertices
				VertexA.add_edge(vertex_b_id, weight)
				# if this is not a digraph, add an edge back
				if graph['type'] == 'graph':
					VertexB.add_edge(vertex_a_id, weight)

			# unexpected length
			else:
				raise
		return graph


	def count_vertices(self):
		return len(self.graph['vertices'])


	def count_edges(self):
		return len(self.get_edges())


	def get_edges(self):
		edge_list = []
		for vertex in self.graph['vertices']:
			# i_key is the starting vertex
			i_key = vertex
			# i_val is the edge list of i_key vertex
			i_val = self.graph['vertices'][vertex]
			for neighbor in i_val.edges:
				# j_key is the list of neighboring vertices
				j_key = neighbor
				# check if this vertex combo is worth adding
				if j_key >= i_key or self.graph['type'] == 'digraph':
					# j_val is the weight of the edge
					j_val = i_val.edges[j_key]
					# check if this graph has weights
					if j_val:
						edge = [i_key, j_key, j_val]
					else:
						edge = [i_key, j_key]
					# add edge to edge_list
					edge_list.append(edge)
		return edge_list


	def textify_edges(self):
		edge_list = self.get_edges()
		final_string = ''
		for edge in edge_list:
			edge_string = ','.join(edge)
			final_string += '('
			final_string += edge_string
			final_string += ')\n'
		return final_string.strip()


	def shortest_path_bfs(self, A, B):
		'''
		A = given starting node
		B = given finishing node
		C = arbitrary iterated node
		a_list = 
		b_list = 
		c_list = 
		queue:
		visited: set of visited vertices
		vertices: every single vertex in the graph
		'''
		vertices = self.graph['vertices']
		# create vertex queue, and start with vertex A
		queue = [[A]] # HACK not a real queue
		# create visited set, and start with vertex A
		visited = {A}

		while queue != []:
			# dequeue first vertex
			# HACK change later for non-array
			a_list = queue.pop()
			A = a_list[-1]
			# check a condition
			if A == B:
				return a_list
			# add its neighbors to the queue
			for C in vertices[A].edges:
				if C in visited:
					pass
				else:
					# visit the vertex
					visited.add(C)
					# HACK change later for non-array
					c_list = a_list[:]
					c_list.append(C)
					queue.insert(0, c_list)
		return []


	def nth_degree_neighbors(self, A, N):
		N = int(N)
		vertices = self.graph['vertices']
		# create visited set, and visit vertex A
		visited = {A}
		# create vertex queue, and start with vertex A
		queue = [[A]] # HACK not a real queue

		# degree trackers
		good_degrees = []
		bad_degrees  = []

		while queue != []:
			# dequeue first vertex
			# HACK change later for non-array
			a_list = queue.pop()
			A = a_list[-1]
			# check a condition
			if len(a_list) == N:
				good_degrees.append(a_list)
			else:
				bad_degrees.append(a_list)
			# add its neighbors to the queue
			for C in vertices[A].edges:
				if C in visited:
					pass
				else:
					# visit the vertex
					visited.add(C)
					# HACK change later for non-array
					n_list = a_list[:]
					n_list.append(C)
					queue.insert(0, n_list)

		# degree trackers
		bad_set = set()
		good_set = set()
		good_final = []
		# bad stuff
		for bad in bad_degrees:
			if len(bad) < N:
				bad_set.add(bad[-1])
		# good stuff
		for good in good_degrees:
			# cant have duplicates
			if good[-1] in good_set:
				pass
			# okay its not a duplicate!
			else:
				good_set.add(good[-1])
				# there's a faster path to this node
				if good[-1] in bad_set:
					pass
				# this is a good node!
				else:
					good_final.append(good)
		return good_final


	def find_largest_clique(self):
		'''
		'''
		# loop through every vertex in graph, named parent
		all_nodes = self.graph['vertices']
		print(all_nodes)
		
		result = self.get_deepest_clique(all_nodes, set(all_nodes), set())
		# ==HACK== flattens nested results
		return set(tuple(sorted(item)) for item in result)


	def get_deepest_clique(self, neighbors, valid_neighbors, visited):
		'''
		# for all children
			# every child must also be a sibling or it is not valid
		# for all siblings
			# every sibling must also be a child or it is not valid
		# we should have valid nodes ripe for a new function
		# create a clique list
		# for each valid, unvisited node
			# visit the node before function call
			# add funciton call of node to clique list
		# return clique list
		'''
		all_nodes = self.graph['vertices']
		# prepare return value
		cliques = set()
		BASE = True
		# validate
		new_valid_neighbors = set(neighbors) & valid_neighbors
		# check base case
		# loop through every valid vertex
		for vertex in new_valid_neighbors:
			if vertex in visited:
				# don't redundently visit vertices
				pass
			else:
				# turn off base case
				BASE = False
				# copy visited to alter in fresh function stack
				new_visited = visited.copy()
				# visit the vertex in this timeline
				new_visited.add(vertex)
				# get new neighbors
				Vertex = all_nodes[vertex]
				new_neighbors = Vertex.edges
				# function call
				result = self.get_deepest_clique(
					new_neighbors, new_valid_neighbors, new_visited)

				# ==HACK==
				# this part is pretty janky
				# just trying to eliminate nested tuples
				if isinstance(result, tuple):
					if isinstance(result[0], tuple):
						for real_result in result:
							cliques.add(real_result)
					else:
						cliques.add(result)
				elif isinstance(result, set):
					for real_result in result:
						cliques.add(real_result)
				else:
					cliques.add(result)

		if BASE:
			visited = tuple(visited)
			print(visited)
			return visited
		else:
			return cliques


	def validate_eulerian(self)
		# run a depth-first search
		# if the current node has the starting point as a neighbor:
			# if every node has been visited:
				# it is a valid eulerian cycle.
			# if not every node has been visited:
				# continue DFS until end.
		# if DFS ends:
			# it is not a valid eulerian cycle.
