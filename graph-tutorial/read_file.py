# internal projects
import sys
import re
# python packages
from vertex import Vertex

def read_file(filepath):
	'''
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
	'''
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
	'''
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
		vertex_a = vertex_dict[vertex_a_id]
		vertex_b = vertex_dict[vertex_b_id]

		# edge has no weight
		if len(edge) == 2:
			# add edge on main vertex
			vertex_a.add_edge(vertex_b_id)
			# if this is not a digraph, add an edge back
			if graph_type == 'graph':
				vertex_b.add_edge(vertex_a_id)

		# edge is weighted
		elif len(edge) == 3:
			# the third item is the weight
			weight = int(edge[2])
			# add edge on both vertices
			vertex_a.add_edge(vertex_b_id, weight)
			# if this is not a digraph, add an edge back
			if graph_type == 'graph':
				vertex_b.add_edge(vertex_a_id, weight)

		# unexpected length
		else:
			raise

def extract(filepath):
	'''
	'''
	graph = {}
	# call helpers
	text_data = read_file(filepath)
	graph_type = get_type(text_data)
	vertex_dict = get_vertices(text_data)
	extract_edges(text_data, graph_type, vertex_dict)
	# return given data
	return graph_type, vertex_dict
