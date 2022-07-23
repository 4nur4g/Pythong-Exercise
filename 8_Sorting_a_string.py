def strsort(string):
    charlist = []
    for i in string:
        charlist.append(i)
    charlist.sort()
    return "".join(charlist)

mystr = "thisisastring"

print(strsort(mystr))

# Better solutino exists using sorted for string