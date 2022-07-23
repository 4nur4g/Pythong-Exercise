def firstlast(modarray):

    if type(modarray) is str:
        return str(modarray[0] + modarray[-1])
    if type(modarray) is list:
        return [modarray[0],modarray[-1]]
    if type(modarray) is tuple:
        return (modarray[0],modarray[-1])
    else:
        return "something wrong"


mylist = [i for i in range(5)]
mytup = (2, 3, 4, 1)
mystr = "changumangu"

inputlist = [mylist,mytup,mystr]

for i in inputlist:
    print(firstlast(i))
    print(type(firstlast(i)))

# could write better code 



# print(mystr[0])
