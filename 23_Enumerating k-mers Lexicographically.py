from itertools import product

def lexicographically_ordered_permutation(symbols, n):
    '''Return all strings of length n that can be formed
    from the provided symbols, ordered lexicographically
    (use the standard order of letters in the English alphabet).'''
    result = []
    for i in product(list(symbols), repeat=n):
        result.append(''.join(list(i)))
    result.sort()
    return result


with open('rosalind_lexf.txt', 'r') as f:
    input = f.read().split('\n')
input[0] = input[0].replace(' ', '')
for i in lexicographically_ordered_permutation(input[0], int(input[1])):
    print(i)
