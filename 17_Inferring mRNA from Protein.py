def num_of_diff_RNA_strings_from_which_protein_could_be_translated(protein_string):
    protein_string = list(protein_string)
    frequency_list = [['Stop', 3]]
    result = 1
    for x in protein_string:
        frequency = 0
        for y in RNA_codon_list:
            if x in y:
                frequency += 1
        frequency_list.append([x, frequency])
    print('Frequency list:', frequency_list)
    for i in frequency_list:
        result *= i[1]
    print('Result = (', ' * '.join([str(i[1]) for i in frequency_list]), ') % 1,000,000 = ', sep = '')
    print('Result =', end = ' ')
    result = result % 1000000
    return result

RNA_codon_list = []

with open('RNA_codon_table.txt', 'r') as f:
    for i in [x.strip('\n') for x in f.readlines()]:
        RNA_codon_list.extend(i.split('      ') and i.split('   '))
while '' in RNA_codon_list:
    RNA_codon_list.remove('')
RNA_codon_list = [i.split(' ') for i in RNA_codon_list]

with open('rosalind_mrna.txt', 'r') as f:
    input = f.read()

print(num_of_diff_RNA_strings_from_which_protein_could_be_translated(input))
