def mortal_rabbit_population(n, m):
    '''Duration in month: n <= 100,
       Lifespan in month: m <= 20'''
    total = [1, 1, 1, 2]
    for i in range(n - 3):
        total.append(sum(total[-m:-1]))
    total.pop(0)
    print('Total population across different generations are\n', total)
    return 'Current population after ' + str(n) + ' generations: ' + str(total[-1])


print(mortal_rabbit_population(84, 19))
