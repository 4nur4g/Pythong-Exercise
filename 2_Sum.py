def mysum(*arg):
    sum = 0
    for i in arg:
        sum += i
    return sum


print(mysum(*[1, 2, 3, 1]))
