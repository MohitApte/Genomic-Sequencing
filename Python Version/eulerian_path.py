#python3
import sys


def get_eulerian_path(graph):
    # Find the starting node
    start_node = list(graph.keys())[0]
    for node in graph:
        out_degree = len(graph[node])
        in_degree = sum([node in graph[neigh] for neigh in graph])
        if out_degree > in_degree:
            start_node = node
            break
        elif out_degree > 0:
            start_node = node

    # Traverse the graph to get the Eulerian path
    euler_path = []
    stack = [start_node]
    while stack:
        node = stack[-1]
        if graph[node]:
            next_node = graph[node][0]
            graph[node].remove(next_node)
            stack.append(next_node)
        else:
            euler_path.append(stack.pop())

    # Reverse the path to get the correct order
    euler_path.reverse()
    return euler_path



if __name__ == "__main__":
    input_list = sys.stdin.read().strip().splitlines()
    graph = {}
    for line in input_list:
        vertex, edges = line.split(' -> ')
        graph[int(vertex)] = [int(v) for v in edges.split(',')]
       
    lst = []
    for i in graph.keys():
        for j in graph[i]:
            if j not in graph:
                lst.append(j)
                
    for i in lst:
        graph[i] = [] 
   

    path = get_eulerian_path(graph)
    print("->".join(map(str, path)))

