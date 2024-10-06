def sum(x):
    sum = 0
    for i in range(x):
        sum += i
    """
    0
    1
    2
    3
    4

    res = 0

    1: 0 + 1 = 1

    2: 1 + 2 = 3

    3: 3 + 3 = 6

    4: 6 + 4 = 10

    """
    return sum
print(sum(6))