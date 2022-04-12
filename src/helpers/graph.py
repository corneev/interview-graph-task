from typing import Dict, List

import enchant


def find_paths(adj: List[List[int]], path=None):
    """
    Generates all existing paths whithin a simple graph.
    An implementation of Depth First Search Algorythm (DSA)
    :param adj: Adjacency matrix
                [[0, 1, 1, 1],
                 [0, 0, 0, 1],
                 [1, 1, 0, 0],
                 [0, 0, 0, 0]]
    """
    if not path:
        for start_node in range(len(adj)):
            yield from find_paths(adj, [start_node])
    else:
        if len(path) >= 2:  # minimal path length is 2
            yield path
        # continue to recur if current location has not been visited before
        if path[-1] in path[:-1]:
            return
        # recursively search for all paths forward from the current node
        current_node = path[-1]
        for next_node in range(len(adj[current_node])):
            if adj[current_node][next_node] == 1:
                yield from find_paths(adj, path + [next_node])


def convert_into_word(path: List[int], lookup_dict: Dict[int, str]) -> str:
    """
    Applies dictionary to convert path into word
    :param path: Vertex sequence Ex.[0, 1, 2, 0]
    :param lookup_dict: Lookup dictionary {vertex: "character"}
    :return: Path's representation as a string
    """
    word = ""
    for vertex in path:
        word = word + lookup_dict[vertex]
    return word


def is_word(word: str) -> bool:
    """
    Check prowided string is an English dictionary word
    pyenchant check() wrapper
    :params word: String to check
    :return: True if it is an English word, and False otherwise.
    """
    d = enchant.Dict("en_US")
    return d.check(word)
