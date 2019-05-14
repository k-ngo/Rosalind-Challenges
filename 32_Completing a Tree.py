def num_of_edges_to_complete_tree(n, pairs):
    """Return the minimum number of edges that can be added to the graph to produce a tree."""
    # Given a *connected* tree of n nodes will always contain n - 1 edges,
    # Min. number of edges to produce a tree, given the amount of pairs, is simply:
    return int(n) - 1 - len(pairs)

with open('rosalind_tree.txt', 'r') as f:
    data = f.read().split('\n')
data = [i.split(' ') for i in data]
n = data[0][0]
pairs = data[1:]

print(num_of_edges_to_complete_tree(n, pairs))

