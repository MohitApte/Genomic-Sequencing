#python3
from collections import defaultdict
import random
import sys

def find_cycle(graph, start):
    """Return a sequence of nodes which form a cycle
    starting from a node 'start'.
    """
    cycle = []
    u = graph[start].pop()
    while u != start:
        cycle.append(u)
        u = graph[u].pop()
    cycle.append(u)

    # Clean up nodes which have no edges.
    toRemove = [k for k, v in graph.items() if not v]
    for k in toRemove:
        del graph[k]

    return cycle

def find_eulerian_cycle(graph, start=0):
    """Return an eulerian cycle of the graph."""
    i = 0
    while i not in graph:
        i += 1
    start = i    
    cycle = [start] + find_cycle(graph, start)
    updated = True
    while updated:
        updated = False
        for i, start in enumerate(cycle):
            # If an edge starting from the node still exists,
            # insert new cycle.
            if start in graph:
                updated = True
                cycle = cycle[:i+1] + find_cycle(graph, start) + cycle[i+1:]
                break

    return cycle



if __name__ == "__main__":
    input_list = sys.stdin.read().strip().splitlines()
    graph = {}
    for line in input_list:
        vertex, edges = line.split(' -> ')
        graph[int(vertex)] = [int(v) for v in edges.split(',')]
    
    cycle = find_eulerian_cycle(graph)
    print("->".join(map(str, cycle)))


        