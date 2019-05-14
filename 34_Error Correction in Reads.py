def err_correction(data):
    """
    Given: A collection of up to 1000 reads of equal length (at most 50 bp) in FASTA format.
    Some of these reads were generated with a single-nucleotide error. For each string in the dataset,
    one of the following applies:
    1. string was correctly sequenced and appears in the dataset at least twice (possibly as a reverse complement);
    2. string is incorrect, it appears in the dataset exactly once, and its Hamming distance
    is 1 with respect to exactly one correct read in the dataset (or its reverse complement).
    Return: a list of all corrections in the form "[old read]->[new read]".
    (Each correction must be a single symbol substitution, and you may return
    the corrections in any order.)
    """

    correct_lst_reg = []
    tmp_data = data[:]
    for i in tmp_data:
        if tmp_data.count(i) > 1 or tmp_data.count(i) + tmp_data.count(rvs_comp(i)) > 1:
            correct_lst_reg.append(i)
            data.remove(i)
    correct_lst_rvs = [rvs_comp(i) for i in correct_lst_reg]
    correct_lst = correct_lst_reg + correct_lst_rvs
    corrections = []
    for i in data:
        for j in correct_lst:
            if hamming_dist(i, j) == 1 and [i, j] not in corrections:
                corrections.append([i, j])
    for i in corrections:
        print(i[0], '->', i[1], sep='', end='\n')
    return

def rvs_comp(DNA):
    """Return the verse complement of a DNA string."""
    result = []
    for i in list(DNA):
        if i == 'A':
            result.append('T')
        elif i == 'T':
            result.append('A')
        elif i == 'C':
            result.append('G')
        elif i == 'G':
            result.append('C')
    result.reverse()
    return ''.join(result)

def hamming_dist(s, t):
    "Return the Hamming distance of 2 strings."
    dist = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            dist += 1
    return dist


with open('rosalind_corr.txt', 'r') as f:
    data = f.read().split('>')
data = [i.split('\n', 1) for i in data if i != '']
data = [i[1].replace('\n', '') for i in data]

err_correction(data)
