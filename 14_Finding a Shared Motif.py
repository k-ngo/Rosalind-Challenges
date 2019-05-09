def longest_common_substring(input):
    result = ''
    string_1 = ''
    record = 1
    # Check for longest string to use as base string to compare against
    for i in input:
        if len(i[1]) > len(string_1):
            string_1 = i[1]
    print('String to compare:', string_1)
    # Search for common substring
    print('Now searching for longest common substring...')
    for index_begin in range(len(string_1)):
        for index_end in range(1, len(string_1) + 1):
            for string_2 in input:
                if string_1 != string_2[1]:
                    segment = string_1[index_begin:index_end]
                    if segment in string_2[1] and len(segment) >= record:
                        # print(segment, 'is in', string_2[1])
                        result = segment
                        record = len(result)
                    else:
                        break
    print('Result:', end = ' ')
    return result


with open('rosalind_lcsm.txt', 'r') as f:
    input = f.read().split('>')
input = [i.replace('\n', ' ') for i in input if i != '']
input = [i.split(' ', 1) for i in input]
input = [[i[0], i[1].replace(' ', '')] for i in input]

print(longest_common_substring(input))
