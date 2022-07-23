def mysum(*something):
    if not something:
        return "please provide the input"
    else:
        sum = something[0]
        for item in something[1:]:
            sum += item
        return sum 


print(mysum()) 
print(mysum(10, 20, 30, 40)) 
print(mysum('a', 'b', 'c', 'd'))
print(mysum([10, 20, 30], [40, 50, 60], [70, 80]))