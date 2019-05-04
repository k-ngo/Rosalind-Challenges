def highest_CG(DNA_strings):
    str_list = []
    result = []
    gc_concentration_max = 0

    for i in DNA_strings.split('>'):
        if i != '':
            str_list.append([ i[:13], i[13:] ])
    for combo in str_list:
        gc_count = 0
        for DNA in combo[1]:
            if DNA == 'G' or DNA == 'C':
                gc_count += 1
        gc_concentration = gc_count / len(combo[1]) * 100
        if gc_concentration > gc_concentration_max:
            gc_concentration_max = gc_concentration
            result = [combo[0], gc_concentration]

    return result

with open('rosalind_gc.txt', 'r') as f:
    input = [i.strip('\n') for i in f.readlines()]
input = ''.join(input)

print('%s\n%f' % (highest_CG(input)[0],highest_CG(input)[1]))

