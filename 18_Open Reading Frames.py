from textwrap import wrap
import re

def convert_DNA_ORF_to_protein(DNA):
    translation_list = []
    # Determine the 6 reading frames from the given DNA string
    # https://en.wikipedia.org/wiki/Reading_frame
    reg_frame_1 = wrap(DNA[:], 3)
    reg_frame_2 = wrap(DNA[1:-2], 3)
    reg_frame_3 = wrap(DNA[2:-1], 3)
    reg_frame_list = [reg_frame_1, reg_frame_2, reg_frame_3]
    DNA_rvs = reverse_complement(DNA)
    rvs_frame_1 = wrap(DNA_rvs[:], 3)
    rvs_frame_2 = wrap(DNA_rvs[1:-2], 3)
    rvs_frame_3 = wrap(DNA_rvs[2:-1], 3)
    rvs_frame_list = [rvs_frame_1, rvs_frame_2, rvs_frame_3]
    frame_list = reg_frame_list + rvs_frame_list
    # Compile all 6 reading frames (start codon: AUG) as nested lists inside 1 list
    for frame in frame_list:
        temp_translation_list = []
        for segment in frame:
            for protein in DNA_codon_list:
                if segment == protein[0]:
                    temp_translation_list.append(protein[1])
        translation_list.append(''.join(temp_translation_list))
    # Search for Open Reading Frames in all nested lists then append to result list
    result = []
    match = re.compile(r'(?=(M(.*?)(Stop)))')
    for string in translation_list:
        match_indices = [[i.start(), i.end(2)] for i in re.finditer(match, string)]
        for i in match_indices:
            if string[i[0]:i[1]] not in result:
                result.append(string[i[0]:i[1]])
    return result

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


DNA_codon_list = []

with open('DNA_codon_table.txt', 'r') as f:
    for i in [x.strip('\n') for x in f.readlines()]:
        DNA_codon_list.extend(i.split('      ') and i.split('   '))

while '' in DNA_codon_list:
    DNA_codon_list.remove('')
DNA_codon_list = [i.split(' ') for i in DNA_codon_list]

with open('rosalind_orf.txt', 'r') as f:
    input = f.read().split('\n')[1:]
input = ''.join(input)

for i in convert_DNA_ORF_to_protein(input):
    print(i)
