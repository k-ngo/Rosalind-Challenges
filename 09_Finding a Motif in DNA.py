def find_motif_in(s, t):
    locations = []
    for i in range(len(s)):
        if s[i:i + len(t)] == t:
            locations.append(i + 1)
            # Adding + 1 to i is purely done so the results
            # match with the '1-based numbering' indexing format
            # as used in the Rosalind challenge instruction.
            # There would be no point to doing it otherwise.
    return ' '.join([str(i) for i in locations])


with open('rosalind_subs.txt', 'r') as f:
    input = [i.strip('\n') for i in f.readlines()]

print(find_motif_in(input[0], input[1]))
