# internal projects
import sys
import re
# python packages
from vertex import Vertex

def read_file(filepath):
	'''
	grabs a text file from given filepath.
	'''
	# initialize empty return value.
	text_data = []
	# read file from the source.
	with open(filepath, 'r') as file:
		text_data = file.readlines()
	# clean text_data by stripping.
	for index, entry in enumerate(text_data):
		text_data[index] = entry.strip()
	return text_data

def get_type(text_data):
	'''
	a graph can be either a graph or digraph.
	if it is not, an error is raised.
	'''
	# get character from text data.
	character = text_data[0].lower()
	# check graph type.
	graph_type = ''
	if character == 'g':
		graph_type = 'graph'
	elif character == 'd':
		graph_type = 'digraph'
	# only two graph types allowed!
	else:
		raise ValueError(
			'\ninvalid graph type.'
			'\ntype must be G for graph,'
			'\nor otherwise D for digraph.'
		)
	return graph_type

def get_vertices(text_data):
	'''
	create a key:value pairing for vertices.
	a single character usually represents a vertices' key.
	the vertex object itself is the full data or value here.
	'''
	if len(text_data) == 1:
		return {}
	# initialize empty return value.
	vertex_dict = {}
	# clean up the given vertex list string.
	vertex_list = text_data[1].split(',')
	# loop through the list; create new vertex from each id.
	for vertex_id in vertex_list:
		vertex_dict[str(vertex_id)] = Vertex(str(vertex_id))
	return vertex_dict

def extract_edges(text_data, graph_type, vertex_dict):
	'''
	gets the list of all edges in the graph.
	these should be laid out at the beginning.
	if a graph vertex has a different name than one of these,
	there is something wrong and an error will be thrown.
	'''
	# populate vertices with edge data.
	edge_list = text_data[2:]
	# loop through every edge.
	for index, edge in enumerate(edge_list):
		# ensure edge starts as expected.
		assert('(' in edge)
		assert(')' in edge)
		# clean edge
		edge = re.sub(r'[\(\)]', '', edge)
		edge = edge.split(',')

		# vertex_a_id/_b_id are just string ids.
		vertex_a_id = str(edge[0])
		vertex_b_id = str(edge[1])

		# these are actual vertex objects.
		vertex_a = vertex_dict[vertex_a_id]
		vertex_b = vertex_dict[vertex_b_id]

		# edge has no weight.
		if len(edge) == 2:
			# add edge on main vertex.
			vertex_a.add_edge(vertex_b_id)
			# if this is not a digraph, add an edge back.
			if graph_type == 'graph':
				vertex_b.add_edge(vertex_a_id)

		# edge is weighted.
		elif len(edge) == 3:
			# the third item is the weight.
			weight = int(edge[2])
			# add edge on both vertices.
			vertex_a.add_edge(vertex_b_id, weight)
			# if this is not a digraph, add an edge back.
			if graph_type == 'graph':
				vertex_b.add_edge(vertex_a_id, weight)

		# unexpected length...
		else:
			raise ValueError(
				'this edge must have 2 or 3 values.'
				'\ninstead, edge is equal to...'
				f'\n{edge}'
			)

def extract(filepath):
	'''
	this extracts many data from a formatted text file.
	it calls upon four other helper functions in this file.
	refer to them for further understanding.
	'''
	graph = {}
	# call helpers
	text_data = read_file(filepath)
	graph_type = get_type(text_data)
	vertex_dict = get_vertices(text_data)
	extract_edges(text_data, graph_type, vertex_dict)
	# return given data
	return graph_type, vertex_dict
