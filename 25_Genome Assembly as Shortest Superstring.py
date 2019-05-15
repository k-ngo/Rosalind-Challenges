def shortest_superstring(lst):
    """Return a shortest superstring containing all the given strings,
    constructed by gluing together longest segments that overlap."""
    # First, we acknowledge that the result will consist of:
    # a prefix + overlapping stuff + a suffix.
    # Determine prefix
    # (string with segment that doesn't overlap by more than half their length from start)
    for i in lst:
        segment = i[:len(i)//2+2]
        tmp_lst = [x for x in lst if x != i]
        for j in tmp_lst:
            if segment not in j and j == tmp_lst[-1]:
                prefix = i
            elif segment in j:
                break
    # Determine suffix
    # (string with segment that doesn't overlap by more than half their length from end)
    for i in lst:
        segment = i[len(i)//2-1:]
        tmp_lst = [x for x in lst if x != i]
        for j in tmp_lst:
            if segment not in j and j == tmp_lst[-1]:
                suffix = i
            elif segment in j:
                break
    print('Prefix:', prefix)
    print('Suffix:', suffix)
    # Eliminate prefix and suffix from list
    lst.remove(prefix)
    lst.remove(suffix)
    # To understand how this part of the code work,
    # please first refer to the usage of function overlap(base, s) below this function.
    # 0. Set the initial result equal to the prefix.
    # 1. Initiate a loop through the list,
    #    Find element i that overlaps the most with the result
    # 2. Set result as overlap(result, i)
    # 3. Remove the element i from the present list.
    # 4. Continue step 1-3 until the list has no elements left.
    result = prefix
    while len(lst) > 0:
        tmp_result = ''
        for index, i in enumerate(lst):
            if len(overlap(result, i)) < len(tmp_result) or index == 0:
                tmp_result = overlap(result, i)
                tmp_result_i = index
        result = tmp_result
        lst.pop(tmp_result_i)
    result = overlap(result, suffix)
    print('Result (length = ', len(result), '):\n', result, sep='')
    return

def overlap(base, s):
    """Concatenate string 'base' with string 's', removing any overlapping characters in between"""
    n = len(s)
    for max_len in range(n-1, -1, -1):
        if s[:max_len+1] in base[-max_len-1:]:
            base += s[max_len+1:]
            return base
    return base + s


with open('rosalind_long.txt', 'r') as f:
    data = f.read().split('>')
data = [i.split('\n', 1) for i in data if i != '']
data = [[i[0], i[1].replace('\n', '')] for i in data]
input = [i[1] for i in data]

shortest_superstring(input)
