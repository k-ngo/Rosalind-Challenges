import re

def find_reverse_palindrome(DNA):
    '''Find instances of reverse palindrome within a DNA string.'''
    result = []
    progress = 0
    print('DNA string:', DNA)
    print('Now searching for instances of reverse palindrome...')
    for index_begin in range(len(DNA)):
        for index_end in range(1, len(DNA) + 1):
            segment = DNA[index_begin:index_end]
            if len(segment) >= 4 and segment == reverse_complement(segment):
                    index = index_begin + 1
                    # With regards to above:
                    # Adding 1 to each index is purely done so the answers will match
                    # with the 1-based indexing format used by Rosalind.
                    # There would be no point to doing it otherwise.
                    length = len(segment)
                    result.append([index, length])
        progress += 1
        print('Progress: ', round(progress/len(DNA)*100, 2), '%', sep = '')
    print('Process completed. Results are displayed below:')
    return result

# 23.65 sec with 1 if no continue
# 23.72 sec with 2 if
def reverse_complement(DNA):
    '''Return the reverse complement of a DNA string'''
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


with open('rosalind_revp.txt', 'r') as f:
    input = f.read().split('\n')
input = ''.join(input[1:])

for i in find_reverse_palindrome(input):
    print(' '.join(map(str, i)))
