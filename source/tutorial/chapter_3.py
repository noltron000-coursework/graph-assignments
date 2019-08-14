# python packages
import os
import sys
import inspect

# get reference of current directory.
currentdir = os.path.dirname(
    os.path.abspath(
        inspect.getfile(
            inspect.currentframe())))
# get reference of parent directory.
parentdir = os.path.dirname(currentdir)
# pull contents from parent directory into current.
sys.path.insert(0, parentdir)

# internal projects
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

    print(graph.nth_degree_neighbors(A, N))
