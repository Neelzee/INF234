"""
Using Kahn's algorithm, I can sort any DAG.
The reason for this, is that, when constructing the Vertex,
you have to supply the vertices that are pointing towards the one you are constructing.
So, given the graph (list), I can sort it, based on the length of _from.

This makes the running time of the algorithm to be `N log N`, since we have to take the length of _from, when sorting, like so: vertices.sort(key = lambda v: len(v._from))-
The big-o of `len()` is `1`.
While the `.sort()` method, has a big-o of `N log N`, making the running time of the entire algorithm, `N log N`. Where `N` is the amount of vertices in the DAG.

This could be called 'cheating', or a useless algorithm, since we need the in-degrees of a Vertex.
If this was to be a realistic, and or usefull algorithm, a Vertex should only keep track of the vertices it is pointing towards, so instead, we can do the following:

1. Change Vertex from needing the vertices that are pointing towards it, to vertices that it is pointing too.

2. Create a function, f(vertices: Graph[Vertex]) -> dict[Vertex, Int]
    2. 1. This function takes in all the vertices in a Graph, and should return a dictionary, of each Vertex, and their corresponding in-degree.
    2. 2. Too achive this, we iterate over all the vertices _v_, and iterate over _v_ 's neighbours (the vertices _v_ is pointing towards). Incrementing their count in the dictionary.
    2. 3. We then use this function, like so: verticies.sort(key = lamba v: dictionary[v]), where dictionary is created by `f`.

3. This gives us a big-o of `N^2`.

Author: Nils Michael Fitjar
"""
from __future__ import annotations
from string import ascii_uppercase

NAME = "name"
NEIGHBOURS = "neighbours"
VERTICES = "vertices"
DESC = "description"
EXPECTED = "expected"


class Vertex:
    """
    A Vertex class
    """

    def __init__(self, name: str, _from: list[str] = None) -> None:
        self.name = name
        """
        Name of the Vertex, used as an identifier when printing.
        """

        self._from: list[str] = [] if _from is None else _from
        """
        List of the names of all the vertices that points too this Vertex
        """

    def __str__(self) -> str:
        return self.name


class Graph(list):
    """
    A Graph class
    """

    def __str__(self) -> str:
        if isinstance(self[0], Vertex):
            return ", ".join({str(e.name) for e in self})
        return super().__str__()




TESTS = [
    {
        NAME: "Base Case 1",
        DESC: "One vertex",
        VERTICES: [Vertex("A")],
        EXPECTED: "A"
    },
    {
        NAME: "Base Case 2",
        DESC: "All vertices connected as a linked list",
        VERTICES: [
            Vertex(
                ascii_uppercase[i], [ascii_uppercase[i + 1]]
                ) for i in range(4)
            ] + [Vertex("E", ["A"])],
        EXPECTED: "A B C D E"
    },
    {
        NAME: "Graph",
        DESC: "A DAG", #Taken from https://www.geeksforgeeks.org/topological-sorting/"
        VERTICES: [
            Vertex("5"),
            Vertex("4"),
            Vertex("2", ["5"]),
            Vertex("0", ["5", "4"]),
            Vertex("3", ["2"]),
            Vertex("1", ["4", "3"])
            ],
        EXPECTED: "5 4 2 3 1 0"
    }
]


def topological_ordering(graph: Graph) -> list[Vertex]:
    """Sorts the given graph into a list of vertices, ordered topolocigally

    Args:
        graph (Graph): graph

    Returns:
        list[Vertex]: vertices
    """
    vertices = graph.copy() # N, No reason to have this, other than that I dont like side-effects
    vertices.sort(key = lambda v: len(v._from)) # N log N
    return vertices


def test(test_case: dict) -> str:
    """Runs the given test, returning a formatted string of the result,
    ready to be printed to the console

    Args:
        test_case (dict): Test Case

    Returns:
        str: Formatted string
    """
    graph = Graph(test_case[VERTICES])
    vertices = topological_ordering(graph)

    pretty_verticies = ", ".join([e.name for e in vertices])

    print(f"DESCRIPTION:\n{test_case[DESC]}\n")
    res = "[]" + "-" * (len(pretty_verticies) + 17) + "[]\n"
    res += f"  TEST: {test_case[NAME]}\n"
    res += f"  EXPECTED RESULT: {test_case[EXPECTED]}\n"
    res += f"  ACTUAL RESULT: {pretty_verticies}\n"
    res += "[]" + "-" * (len(pretty_verticies) + 17) + "[]\n"

    return res



def main():
    for test_case in TESTS:
        print(test(test_case))

if __name__ == "__main__":
    main()
