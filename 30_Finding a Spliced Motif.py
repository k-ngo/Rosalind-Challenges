def spliced_motif(s, t):
    """Return one collection of indices of s in which
    the symbols of t appear as a subsequence of s.
    If multiple solutions exist, you may return any one."""
    t = list(t)
    result = []
    index = 0
    for i in t:
        for j_i, j in enumerate(s[index:]):
            if i == j:
                result.append(index + j_i)
                index += j_i + 1
                break
    print(*[i + 1 for i in result]) # Adding 1 to index is only to satisfy Rosalind's 1-based indexing format.
    return


with open('rosalind_sseq.txt', 'r') as f:
    data = f.read().split('>')
data = [i.split('\n', 1) for i in data if i != '']
data = [[i[0], i[1].replace('\n', '')] for i in data]
s = data[0][1]
t = data[1][1]

spliced_motif(s, t)
