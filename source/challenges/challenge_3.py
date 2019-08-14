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


def main(graph, start, finish):
    '''
    CHALLENGE 3
    -----------
    this function parses a graph from a special text file.
    next, it finds the shortest path in this graph.
    once this is done, a textual summary is returned.
    the summary includes a few points:
    - if there is a path that exists between start and finish.
    - the vertices in the path that was found.
    '''
    # grab variables for our summary
    shortest_path = graph.shortest_path_dfs(start, finish)
    # check true or false
    if shortest_path != []:
        path_exists = True
    else:
        path_exists = False

    # summary is a multi-line output
    summary = '' \
        f'There exists a path between' \
        f' vertex {start} and {finish}:' \
        f' {str(path_exists).upper()}\n'
    # gotta check if the path even exists!
    if path_exists:
        summary += '' \
            f'Vertices in the path: {shortest_path}\n'

    # return the summary
    return summary


if __name__ == '__main__':
    # no filepath -- ask for a string
    if len(sys.argv) == 1:
        start = input('input 1st node: ')
        finish = input('input 2nd node: ')
        output = main(Graph(), start, finish)
    elif len(sys.argv) == 2:
        file = sys.argv[1]
        start = input('input 1st node: ')
        finish = input('input 2nd node: ')
        output = main(Graph(file), start, finish)
    elif len(sys.argv) == 3:
        start = sys.argv[1]
        finish = sys.argv[2]
        output = main(Graph(), start, finish)
    # looks like we got a filepath!
    elif len(sys.argv) == 4:
        file = sys.argv[1]
        start = sys.argv[2]
        finish = sys.argv[3]
        output = main(Graph(file), start, finish)
    # there was a problem D:
    else:
        raise

    print(output)
