"""
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
            Vertex("5", ["2", "0"]),
            Vertex("4", ["0", "1"]),
            Vertex("2", ["3"]),
            Vertex("0"),
            Vertex("3", ["1"]),
            Vertex("1")
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
    vertices = [(v.name, len(v._from)) for v in graph] # N
    vertices.sort(key = lambda x: x[1]) # N log N
    return vertices[::-1]


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

    pretty_verticies = ", ".join([e[0] for e in vertices])

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
