string = input()
leng = len(string)
a = string[0]
b = string[1]

for i in range(leng):
    if string[i] == b:
        string = string[:i] + a +string[i + 1:]

print(string)