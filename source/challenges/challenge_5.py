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


def main(Object):
    boolean = str(Object.eulerian_degree()).upper()
    return f'This graph is Eulerian: {boolean}'


if __name__ == '__main__':
    # no filepath -- ask for a string
    if len(sys.argv) == 1:
        output = main(Graph())

    # have a filepath
    elif len(sys.argv) == 2:
        file = sys.argv[1]
        output = main(Graph(file))

    # there was a problem!
    else:
        raise ValueError()

    print(output)
