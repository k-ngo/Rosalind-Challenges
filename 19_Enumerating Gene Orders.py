from itertools import permutations

def permutation(n):
    result = []
    int_list = [i for i in range(1, n + 1)]
    for i in permutations(int_list, n):
        result.append(list(i))
    return result


n = 5 # Length of permutation
print(len(permutation(n))) # Number of possible permutations
for i in permutation(n):
    print(' '.join(map(str, i)))
