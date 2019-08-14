import unittest
from graph import Graph
from vertex import Vertex

class VertexTest(unittest.TestCase):
	def test_init(self):
		name = '🙂'
		vertex = Vertex('🙂')
		assert vertex.name is name

class GraphTest(unittest.TestCase):
	def test_empty_graph(self):
		graph = Graph('./source/data/test_empty.txt')
		assert graph.count_edges() == 0
		assert graph.count_vertices() == 0

	def test_single_vertex(self):
		graph = Graph('./source/data/test_single.txt')
		assert graph.count_edges() == 0
		assert graph.count_vertices() == 1

	def test_shortest_path(self):
		graph = Graph('./source/data/network.txt')
		short = graph.shortest_path_dfs('A','N')
		print(short)
		assert short == ['A', 'J', 'K', 'L' ,'M' ,'N']
