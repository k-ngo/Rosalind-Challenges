def consensus(input):

    count_A = []
    count_C = []
    count_G = []
    count_T = []
    profile_matrix = []
    consensus_list = []

    matrix = [list(i[1]) for i in input]
    matrix_transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    matrix_transpose = [''.join(i) for i in matrix_transpose]
    for i in matrix_transpose:
        count_A.append(i.count('A'))
        count_C.append(i.count('C'))
        count_G.append(i.count('G'))
        count_T.append(i.count('T'))

    profile_matrix.extend([count_A, count_C, count_G, count_T])
    profile_matrix_transpose = [[profile_matrix[j][i] for j in range(len(profile_matrix))] for i in range(len(profile_matrix[0]))]
    profile_matrix_transpose = [''.join([str(x) for x in i]) for i in profile_matrix_transpose]
    for i in profile_matrix_transpose:
        if i.index(max(i)) == 0:
            consensus_list.append('A')
        if i.index(max(i)) == 1:
            consensus_list.append('C')
        if i.index(max(i)) == 2:
            consensus_list.append('G')
        if i.index(max(i)) == 3:
            consensus_list.append('T')

    print(''.join(consensus_list))
    print('A:', ' '.join([str(i) for i in profile_matrix[0]]))
    print('C:', ' '.join([str(i) for i in profile_matrix[1]]))
    print('G:', ' '.join([str(i) for i in profile_matrix[2]]))
    print('T:', ' '.join([str(i) for i in profile_matrix[3]]))

    return


with open('rosalind_cons.txt', 'r') as f:
    str_list = ''.join([i.strip('\n') for i in f.readlines()])
input = []
for i in str_list.split('>'):
    if i != '':
        input.append([ i[:13], i[13:] ])
consensus(input)
