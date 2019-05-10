from textwrap import wrap

def RNA_splice(DNA):
    '''Return a protein string resulting from transcribing and translating the exons of a DNA string'''
    # Remove all introns from DNA string
    intron_list = [i[1] for i in DNA[1:]]
    exons = DNA[0][1]
    for intron in intron_list:
        exons = exons.replace(intron, '')
    # Transcribe exons to RNA
    RNA = exons.replace('T', 'U')
    # Translate to proteins
    result = convert_RNA_to_protein(RNA)
    return result

def convert_RNA_to_protein(RNA):
    protein = []
    RNA = wrap(RNA, 3)
    for x in RNA:
        for y in RNA_codon_list:
            if x == y[0]:
                if y[1] != 'Stop':
                    protein.append(y[1])
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

input = []
with open('rosalind_splc.txt', 'r') as f:
    data = f.read().split('>')
for i in data:
    if i != '':
        i = i.split('\n', 1)
        input.append([i[0], i[1].replace('\n', '')])

print(RNA_splice(input))
