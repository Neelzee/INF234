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


class Vertex(dict):
    """
    A Vertex class
    """

    def __str__(self) -> str:
        if NAME in self.keys():
            return self[NAME]
        return super().__str__()


class Graph(list):
    """
    A Graph class
    """

    def __str__(self) -> str:
        return ", ".join({str(e[NAME]) for e in self})




def create_vertex(name: str, neighbours: list[str] = None) -> Vertex:
    """Creates a vertex dict

    Args:
        name (str): Name of the vertex
        neighbours (list[str]): List of the names of the neighbouring nodes.
        In this case, a neighbour, are nodes this vertex is pointing too.

    Returns:
        Vertex: Vertex instance
    """
    return {
        NAME: name,
        NEIGHBOURS: [] if neighbours is None else neighbours
    }

TESTS = [
    {
        NAME: "Base Case 1",
        DESC: "One vertex",
        VERTICES: [create_vertex("A")],
        EXPECTED: "A"
    },
    {
        NAME: "Base Case 2",
        DESC: "All vertices connected as a linked list",
        VERTICES: [
            create_vertex(
                ascii_uppercase[i], [ascii_uppercase[i + 1]]
                ) for i in range(4)
            ] + [create_vertex("E", ["A"])],
        EXPECTED: "A B C D E"
    },
    {
        NAME: "Graph",
        DESC: "A DAG", #Taken from https://www.geeksforgeeks.org/topological-sorting/"
        VERTICES: [
            create_vertex("5", ["2", "0"]),
            create_vertex("4", ["0", "1"]),
            create_vertex("2", ["3"]),
            create_vertex("0"),
            create_vertex("3", ["1"]),
            create_vertex("1")
            ],
        EXPECTED: "5 4 2 3 1 0"
    }
]

def calculate_degrees(graph: Graph) -> dict[Vertex, int]:
    """Calculates the in-degrees to each vertex in the given graph

    Args:
        graph (Graph): Graph

    Returns:
        dict[Vertex, int]: Dict of the calulations
    """
    dag = {n[NAME]: 0 for n in graph}

    for vertex in graph: # N
        for sub_vertex in vertex[NEIGHBOURS]: # N
            dag[sub_vertex] += 1 # 1

    return dag


def topological_ordering(graph: Graph) -> list[Vertex]:
    """Sorts the given graph into a list of vertices, ordered topolocigally

    Args:
        graph (Graph): graph

    Returns:
        list[Vertex]: vertices
    """
    dag = calculate_degrees(graph) # N²
    vertices = graph.copy()
    vertices.sort(key = lambda x: dag[x[NAME]] if x[NAME] in dag.keys() else 0) # N log N
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

    pretty_verticies = str(Graph(vertices))

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
