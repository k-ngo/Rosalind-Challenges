def rabbit_population(n, k):
    '''Duration in month: n <= 40,
       Offspring produced per pair each month: k <= 5'''
    adult_pairs = 0
    child_pairs = 1
    total_pairs = adult_pairs + child_pairs
    for i in range(2, n + 1):
        adult_pairs += child_pairs
        child_pairs = (total_pairs - child_pairs) * k
        total_pairs = adult_pairs + child_pairs
    return total_pairs


print(rabbit_population(30, 3))
