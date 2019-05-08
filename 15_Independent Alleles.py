from math import factorial as fac

def prob_of_at_least_Aa_Bb(k, n):
    '''Probability of at least n children having Aa Bb in the k generation
       Using Punnett Square, we can infer that:
       The prob. of success (p, i.e. offspring w/ AaBb from a couple with AaBb and AaBb) is: 0.25
       The prob. of failure (q, i.e. offspring w/o AaBb from a couple with AaBb and AaBb) is: 0.75
       The amount of offsprings produced each generation is 2^k. This will be the amount of trials.
       The problem is NOT asking for the probability of n children P(n), which can be
       obtained using the Bernoulli's formula for the binomial distribution,
       but it is asking for the probability of *at least* n children.
       This probability is given by:
       P(n) + P(n+1) + P(n+2) + ... + P(2^k)
       where P(n) = (2^k)!/(n!*(2^k-n)!) * 0.25^n * 0.75^(2^k-n)'''
    prob = 0
    for i in range(n, 2**k + 1):
        prob += (fac(2**k)/(fac(i)*fac(2**k-i))) * 0.25**i * 0.75**(2**k - i)
    return prob


print(prob_of_at_least_Aa_Bb(6, 15))
