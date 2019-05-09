def protein_mass(protein_string):
    '''Return protein mass given a protein string.'''
    result = []
    protein_string = list(protein_string)
    for amino_acid_residue in protein_string:
        for mass in mass_table:
            if amino_acid_residue == mass[0]:
                result.append(mass[1])
    return sum(map(float, result))


with open('monoisotopic_mass_table.txt', 'r') as f:
    mass_table = f.read().split('\n')
mass_table = [i.split('   ') for i in mass_table]

with open('rosalind_prtm.txt', 'r') as f:
    input = f.read()

print(protein_mass(input))
