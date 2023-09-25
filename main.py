"""
Author: Nils Michael Fitjar
"""
from __future__ import annotations


class Vertex(dict):
    """
    A Vertex class
    """


class Graph(set):
    """
    A Graph class
    """

NAME = "name"
NEIGHBOURS = "neighbours"


def create_node(name: str, neighbours: list[str]) -> Vertex:
    """Creates a node dict

    Args:
        name (str): Name of the node
        neighbours (list[str]): List of the names of the neighbouring nodes.
        In this case, a neighbour, are nodes this node is pointing too.

    Returns:
        Vertex: Vertex instance
    """
    return {
        NAME: name,
        NEIGHBOURS: neighbours
    }



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
            dag[sub_vertex[NAME]] += 1 # 1

    return dag


def topological_ordering(graph: Graph) -> list[Vertex]:
    """Sorts the given graph into a list of vertices, ordered topolocigally

    Args:
        graph (Graph): graph

    Returns:
        list[Vertex]: vertices
    """
    dag = calculate_degrees(graph) # N²
    vertices = list(graph)
    return vertices.sort(key = lambda x: dag[x[NAME]]) # N log N