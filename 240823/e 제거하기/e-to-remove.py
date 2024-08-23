string = input()
e = string.index('e')

string = string[:e] + string[e + 1:]
print(string)