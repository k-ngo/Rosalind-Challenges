def num_subsets(n):
    """Return the number of subsets of a set with n elements."""
    return 2**n % 1000000


print(num_subsets(855))
