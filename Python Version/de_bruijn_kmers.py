#python3
import sys


def de_bruijn(patterns):
    """Creates a de Bruijn graph from a collection of k-mers

    Args:
        patterns:       a list of strings containing the k-mer collecion
                        to be made into a de Bruijn graph

    Returns:
        a string containing an adjacency list representation of the de Bruijn
        graph as described in the problem specification
    """
    # TODO: your code here
    kmers = patterns
    k = len(kmers[0])
    graph = {}
    for i in range(len(kmers)):
        try:
            graph[kmers[i][:-1]].append(kmers[i][1:])
        except:
            graph[kmers[i][:-1]] = [kmers[i][1:]]
    return graph
    


if __name__ == "__main__":
    patterns = sys.stdin.read().strip().splitlines()
    graph = de_bruijn(patterns)
    print (*(sorted([key + ' -> ' + ','.join(sorted([v for v in value]))
                       for key, value in graph.items()])),sep ='\n')
