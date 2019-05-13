def transition_transversion_ratio(s, t):
    """Return the transition/transversion ratio R(s, t)
    for two DNA strings s and t of equal length."""
    transition = 0
    transversion = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            if (s[i] in 'AG' and t[i] in 'AG') or (s[i] in 'CT' and t[i] in 'CT'):
                transition += 1
            else:
                transversion += 1
    return transition/transversion


with open('rosalind_tran.txt', 'r') as f:
    data = f.read().split('>')
data = [i.split('\n', 1) for i in data if i != '']
data = [[i[0], i[1].replace('\n', '')] for i in data]
s = data[0][1]
t = data[1][1]

print(transition_transversion_ratio(s, t))
