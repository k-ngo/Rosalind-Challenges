def overlap_graph(input, k):
    result = []
    for i in input:
        for x in input:
            if i != x:
                # Case: Prefix to Suffix
                if i[1][0:k] == x[1][-k:] and [x[0], i[0]] not in result:
                    result.append([x[0], i[0]])
                # Case: Suffix to Prefix
                if i[1][-k:] == x[1][0:k] and [i[0], x[0]] not in result:
                    result.append([i[0], x[0]])
    return result


with open('rosalind_grph.txt', 'r') as f:
    input = f.read().split('>')
while '' in input:
    input.remove('')
input = [i.split('\n') for i in input]
input = [[i[0], ''.join(i[1:])] for i in input]

for i in overlap_graph(input, 3):
    print(i[0], i[1])
