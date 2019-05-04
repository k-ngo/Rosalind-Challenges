def dom_phenotype(input):
    result = 0
    for i in range(len(input)):
        result += int(input[i]) * dominant_genotype_chance[i][1]
    return int(result * 2)


dominant_genotype_chance = [
    ['AA-AA', 1],
    ['AA-Aa', 1],
    ['AA-aa', 1],
    ['Aa-Aa', 0.75],
    ['Aa-aa', 0.5],
    ['aa-aa', 0]
] # Obtained using Punnett Square

input = '16067 18443 17566 16720 17898 19118'
input = input.split(' ')
print(dom_phenotype(input))
