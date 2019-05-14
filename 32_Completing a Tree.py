def num_of_edges_to_complete_tree(n, pairs):
    """Return the minimum number of edges that can be added to the graph to produce a tree."""
    return int(n) - len(pairs) - 1

with open('rosalind_tree.txt', 'r') as f:
    data = f.read().split('\n')
data = [i.split(' ') for i in data]
n = data[0][0]
pairs = data[1:]

print(num_of_edges_to_complete_tree(n, pairs))

