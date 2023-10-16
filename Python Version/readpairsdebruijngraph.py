#!/usr/bin/env python
# coding: utf-8

# In[94]:


data = "".join(open('data.txt')).split()
pairs = data[2:] # read until we see output line
d = int(data[1])
print(d, pairs[0], pairs[1], "...", sep="\n")


# In[95]:


print(data)


# In[96]:


import numpy as np
def deBruijn(read_pairs):
    # first construct a dictionary where each [(vertex1) ---(edge)--> (vertex2)] is a key-value 
    # pair in this dictionary where vertex1 is key and vertex2 is a value corresponding to that key
    # !!! This dictioary serves as de Bruijn graph in my implementation.
    edges = {}
    for pair in read_pairs:
        # first split each line into suffixes and prefixes by removing first and last elements
        split_point = pair.index('|')
        first_part = (pair[:split_point-1], pair[split_point+1:-1])
        second_part =  (pair[1:split_point], pair[split_point+2:])
        # add this to dictionary
        if first_part not in edges.keys(): 
            edges[first_part] = []
        edges[first_part].append(second_part)
    # after constructing the dictionary, construct adjacency matrix and column-row names of this matrix
    adj_matrix_column_names = list(edges.keys()) ## add sources
    for key in edges.keys(): ## add sinks
        print(edges[key])
        adj_matrix_column_names.append(*edges[key])
    adj_matrix_column_names = list(set(adj_matrix_column_names))## remove duplicates
    adj_matrix_column_names.sort() ## sort lexicographically
    adj_matrix = [[0]*len(adj_matrix_column_names) for i in range(len(adj_matrix_column_names))]
    for i,key in enumerate(adj_matrix_column_names):
        try: ## to deal with key not found error
            for val in edges[key]:
                adj_matrix[i][adj_matrix_column_names.index(val)] = 1
        except KeyError:
            continue
    return edges, np.array(adj_matrix), adj_matrix_column_names


# In[97]:


edges, adj_matrix, adj_matrix_column_names = deBruijn(pairs)


# In[98]:


def print_matrix(matrix):
    for row in matrix[:20]:
        for el in row[:20]:
            # print 1's in red so that you can distinguish easily :)
            print('\x1b[0;31;47m' + str(el) + '\x1b[0m', end= "  ") if el else print(el,end="  ")
        print()


# In[99]:


print_matrix(adj_matrix)


# In[100]:


tail_pair_index = np.where(adj_matrix.sum(axis=1) == 0)[0][0]
head_pair_index = np.where(adj_matrix.sum(axis=0) == 0)[0][0]
adj_matrix[tail_pair_index][head_pair_index] = 1
edges[adj_matrix_column_names[tail_pair_index]] = [adj_matrix_column_names[head_pair_index]]


# In[101]:


def findEulearianCycle():
    path = [adj_matrix_column_names[0]] # start from a random vertex, I chose first of the lexicographical order.
    cycle = [] # hold the cycle
    while path: # while not empty, equivalent to whether we came the vertex above (since we remove edges going out of a vertex in each step)
        vertex = path[-1]
        if vertex in edges and edges[vertex]: # if there is an edge going out from this vertex
            next_v = edges[vertex].pop()
            path.append(next_v)
        else:
            cycle.append(path.pop())
    return cycle[::-1][:-1] # reverse the cycle and remove the last element since it appears on both head and tail of the cycle
eulearian_cycle = findEulearianCycle()


# In[102]:


head_index = eulearian_cycle.index(adj_matrix_column_names[head_pair_index])
eulearian_cycle = eulearian_cycle[head_index:] + eulearian_cycle[:head_index]
print(eulearian_cycle[0], "-> ... ->", eulearian_cycle[-1])


# In[103]:


reconstructed_genome = eulearian_cycle[0][0] # start with first
for paired_k_mer in eulearian_cycle[1: d + 2]: # append last element of the prefixes of first d+1 k-mer pairs
    reconstructed_genome += paired_k_mer[0][-1]
reconstructed_genome += eulearian_cycle[0][1] # append last element of the suffixes of remaining k-mer pairs
for paired_k_mer in eulearian_cycle[1:]:
    reconstructed_genome += paired_k_mer[1][-1]


# In[104]:


reconstructed_genome


# In[ ]:





# In[ ]:





# In[ ]:




