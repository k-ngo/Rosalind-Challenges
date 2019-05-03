from textwrap import wrap

def convert_RNA_to_protein(rna):
    protein = []
    rna = wrap(rna, 3)
    for i in rna:
        for x in RNA_codon_list:
            if i == x[0]:
                if x[1] != 'Stop':
                    protein.append(x[1])
                else:
                    return ''.join(protein)
    return ''.join(protein)


RNA_codon_list = []

with open('RNA_codon_table.txt', 'r') as f:
    for i in [x.strip('\n') for x in f.readlines()]:
        RNA_codon_list.extend(i.split('      ') and i.split('   '))
while '' in RNA_codon_list:
    RNA_codon_list.remove('')
RNA_codon_list = [i.split(' ') for i in RNA_codon_list]

with open('rosalind_prot.txt', 'r') as f:
    input = ''.join([i.strip('\n') for i in f.readlines()])

print(convert_RNA_to_protein(input))
