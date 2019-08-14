# internal projects
import sys
import re
# python packages
from vertex import Vertex
from read_file import read_file, extract

class Graph:
	'''
	this class creates a graph or digraph.
	a graph is like a tree, but allows cycles and loops.
	its methods allow certain checks and passes on the graph.
	'''

	def __init__(self, filepath=None):
		'''
		takes in an optional filepath.
		if none is given, a user can input the filepath.
		by the end of it all, the graph's parameters are found.
		'''
		# check up on the option param.
		if not filepath:
			filepath = input('input the filepath to a graph: ')
		# run extract from read_file.
		self.type, self.graph = extract(filepath)

	def __repr__(self):
		'''
		a graph has many fascets.
		its important to properly represent them all.
		this gives an overview of a graph's properties,
		especially when printed to terminal.
		'''
		# grab variables for our summary.
		graph_type = self.type
		vert_count = self.count_vertices()
		edge_count = self.count_edges()
		edge_list  = self.textify_edges()

		# summary is a multi-line output.
		summary = '' \
		f'Graph Type: {graph_type}\n' \
		f'# Vertices: {vert_count}\n' \
		f'# Edges: {edge_count}\n' \
		f'Edge List:\n{edge_list}\n'

		return summary

	def count_vertices(self):
		'''
		returns the number of vertices in the graph.
		'''
		return len(self.graph)

	def count_edges(self):
		'''
		returns the number of edges in the graph.
		'''
		return len(self.get_edges())

	def get_edges(self):
		'''
		retrieves every single edge in the graph.
		in a digraph, pointing two ways counts as two edges.
		in a graph, pointing two ways counts as just one edge.
		this is due to the nature of these types of graphs.
		---
		root_vrtx represents the root vertex
		root_edges lists all edges of root_vrtx
		ngbr_vrtx represents the neighbor vertex
		edge_weight is the weight of the edge
		'''
		edge_list = []
		for vertex in self.graph:
			# root_vrtx is the starting vertex
			root_vrtx = vertex
			# root_edges is the edge list of root_vrtx vertex
			root_edges = self.graph[vertex]
			for ngbr_vrtx in root_edges.edges:
				# check if this vertex combo is worth adding
				if ngbr_vrtx >= root_vrtx or self.type == 'digraph':
					# edge_weight is the weight of the edge
					edge_weight = root_edges.edges[ngbr_vrtx]
					# check if this graph has weights
					if edge_weight:
						edge = [root_vrtx, ngbr_vrtx, edge_weight]
					else:
						edge = [root_vrtx, ngbr_vrtx]
					# add edge to edge_list
					edge_list.append(edge)
		return edge_list

	def textify_edges(self):
		'''
		this function groups up each edge;
		then represents them in a string.
		---
		each edge is represented by one of these:
		(start, finish)
		(start, finish, weight)
		---
		a digraph has both A->B and B->A if it goes two ways.
		a graph has just A<->B to represent a two way edge.
		'''
		# get full list of edges from a helper function.
		edge_list = self.get_edges()
		# initialize empty return value
		final_string = ''
		# loop through all edges and clean them up
		for edge in edge_list:
			# stringifying integers and floats
			edge = list(str(item) for item in edge)
			# adding string information
			edge_string = ','.join(edge)
			final_string += '('
			final_string += edge_string
			final_string += ')\n'
		# return final value without extra end spaces.
		return final_string.strip()

	def shortest_path_bfs(self, start, finish):
		'''
		this finds the shortest path using breadth-first search.
		---
		start: given starting node
		finish: given finishing node
		between: arbitrary iterated node
		---
		queue: an in-order line of vertices to visit
		visited: set of visited vertices
		vertices: every single vertex in the graph
		'''
		vertices = self.graph
		# create vertex queue, and start with vertex start
		queue = [[start]] # HACK not a real queue
		# create visited set, and start with vertex start
		visited = {start}

		# raise a key error if start or finish is not in the dict.
		if start not in vertices:
			raise KeyError(start)
		if finish not in vertices:
			raise KeyError(finish)

		while queue != []:
			# dequeue first vertex
			# HACK change later for non-array
			start_list = queue.pop()
			start = start_list[-1]
			# check a condition
			if start == finish:
				return start_list
			# add its neighbors to the queue
			for between in vertices[start].edges:
				if between in visited:
					pass
				else:
					# visit the vertex
					visited.add(between)
					# HACK change later for non-array
					between_list = start_list[:]
					between_list.append(between)
					queue.insert(0, between_list)
		else:
			# if it reaches the end without returning,
			# start is on a graph island from finish.
			return []

	def shortest_path_dfs(self, start, finish, path=None, solutions=None):
		'''
		this returns a boolean based on whether two nodes
		are connected (True) or disconnected (False).
		'''
		vertices = self.graph
		if not solutions:
			solutions = []
		else:
			solutions = solutions.copy()
		if not path:
			path = [start]

		# raise key error if start/finish are not vertices.
		if start not in vertices:
			raise KeyError(start)
		if finish not in vertices:
			raise KeyError(finish)

		# iterate through neighbors.
		for between in vertices[start].edges:
			# check if between is the finish line.
			if between == finish:
				path.append(between)
				solutions.append(path)
			# check if between is already in path.
			elif between in path:
				pass
			# otherwise recursively call the new path.
			else:
				new_path = path.copy()
				new_path.append(between)
				new_path = self.shortest_path_dfs(between, finish, new_path, solutions)
				# if its not empty, its a success!
				if new_path != []:
					solutions.append(new_path)

		# we now have an array of our solutions.
		if len(solutions) == 0:
			# there is no solution :(
			return []
		else:
			# we have many solutions.
			# pick the shortest one!
			min_path = min(solutions, key=lambda x: len(x))
			return min_path

	def nth_degree_neighbors(self, A, N):
		'''
		given a node, this function finds every neighbor
		that is no closer than n steps away, 
		but is not further than n steps away.
		---
		its worded this way to show that, if your neighbor 
		is next door, you can't say they are 100 miles away 
		by driving 100 miles in a circle to their house.
		they are considered just next door.
		'''
		N = int(N)
		vertices = self.graph
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
		all_nodes = self.graph
		print(all_nodes)
		
		result = self.get_deepest_clique(
			all_nodes, set(all_nodes), set())
		# ==HACK== flattens nested results
		return set(tuple(sorted(item)) for item in result)

	def get_deepest_clique(self, neighbors, valid_neighbors, visited):
		'''
		'''
		all_nodes = self.graph
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

	def eulerian_degree(self):
		'''
		this function simply ensures that every 
		vertex has an even number of neighbors.
		'''
		# check every vertex in the graph.
		for vertex in self.graph:
			# see if it has an even # of edges.
			if len(self.graph[vertex].edges) % 2 == 0:
				pass
			else:
				# it is not eulerian if it doesnt.
				return False
		else:
			# if the loop ends, it is eulerian.
			return True

	def loop_cycle(self):
		# asdf
		if len(self.graph) != 0:
			result = self.eulerian_recycle()
			return result
		else:
			raise

	def loop_recycle(self, visited=None, vertex=None, goal=None):
		'''
		This is a "Depth-First Search" algorithm.
		Traverse this binary tree recursively, pre-order.
		To do so, visit the given node.
		Then, visit it's left & right children.
		---
		best & worst case runtime: O(n)
		--> we must traverse every node to visit them all.
		~~~
		best & worst case memory usage: O(1)
		--> there is hardly any memory usage - its really 
				contingent on whatever visit(node) does.
		--> note that, being recursive, it could be O(ln(n))
				TODO ↑ this above statement is important, read into
		'''
		# the graph is a collection of vertices.
		graph = self.graph

		# initialize variables on first function call
		if not visited:
			# visited stores all visited items; starts empty.
			visited = set()

		# create a copy of visited list; original must be kept
		visited = visited.copy()

		# create the goal if it doesn't exist.
		if not vertex and not goal:
			# the 1st vertex is some random vertex on the graph.
			vertex = next(iter(graph))
			# the goal is just the starting vertex!
			goal = vertex

		# visit current vertex by adding it.
		visited.add(vertex)
		# create a selection of unvisited vertices
		unvisited = set(list(graph.keys())) - visited

		# check each neighbor
		for neighbor in graph[vertex].edges:
			# base case ~ there is a loop!
			if neighbor == goal and len(unvisited) == 0:
				return True
			# base case ~ neighbor was visited.
			elif neighbor in visited:
				pass
			# revisit function!!
			else:
				return self.eulerian_traversal(visited, neighbor, goal)
		# the loop finished. must have been a bad lead!
		else:
			return False
