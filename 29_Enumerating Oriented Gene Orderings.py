from itertools import permutations

def signed_permutations(n):
    """Return the total number of signed permutations of
    length n, followed by a list of all such permutations
    (you may list the signed permutations in any order)."""
    perm_lst = [i for i in range(-n, n + 1) if i != 0]
    result = []
    for perm in permutations(perm_lst, n):
        if check_if_positive_and_negative_of_elem_exist_in(list(perm)) == False:
            result.append(list(perm))
    print(len(result))
    for i in result:
        print(*i)
    return

def check_if_positive_and_negative_of_elem_exist_in(lst):
    """Check for for every number n, there exists -n within the list.
    If yes, return true.
    If no, return false."""
    for elem in lst:
        if lst.count(elem) + lst.count(-elem) > 1:
            return True
    return False


signed_permutations(5)
