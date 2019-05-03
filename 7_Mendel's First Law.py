def prob_of_dominant_allele(k, m, n):
    '''k = homozygous dominant
       m = heterozygous
       n = homozygous recessive'''
    total_dominant = 2 * k + m
    total_recessive = 2 * n + m
    total_alleles = 2 * (k + m + n)
    prob_XX = total_dominant / total_alleles * (total_dominant - 1) / (total_alleles - 1)
    prob_xX = total_recessive / total_alleles * (total_dominant) / (total_alleles - 1)
    prob_Xx = total_dominant / total_alleles * total_recessive / (total_alleles - 1)
    return prob_XX + prob_xX + prob_Xx

print(prob_of_dominant_allele(15, 24, 16))
