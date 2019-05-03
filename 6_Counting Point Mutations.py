def hamming_dist(s, t):
    dist = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            dist += 1
    return dist

with open('rosalind_hamm.txt', 'r') as f:
    input = [i.strip('\n') for i in f.readlines()]

print(hamming_dist(input[0], input[1]))


