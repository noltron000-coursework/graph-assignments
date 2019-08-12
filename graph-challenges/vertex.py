class Vertex:
	'''
	'''
	def __init__(self, vertex_id):
		self.edges = {}

	def __repr__(self):
		return f'EDGES-->{str(self.edges)}'

	def add_edge(self, vertex_id, weight=None):
		self.edges[vertex_id] = weight