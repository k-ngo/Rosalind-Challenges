from math import factorial as fac

def num_perfect_matchings(string):
    """Return the total possible number of perfect matchings
    of basepair edges in the bonding graph of s."""
    return fac(string.count('A')) * fac(string.count('C'))


with open('rosalind_pmch.txt', 'r') as f:
    data = f.read().split('>')
data = [i.split('\n', 1) for i in data if i != '']
data = [[i[0], i[1].replace('\n', '')] for i in data]
input = data[0][1]

print(num_perfect_matchings(input))
