str1 = input()
str2 = input()
idx1, idx2 = 0, 0
a = []
b = []

for elem in str1:
    if elem >= '0' and elem <= '9':
        idx1 = 1
    else:
        idx1 = 0

    if idx1 == 1:
        a.append(elem)

a = ''.join(a)

for elem in str2:
    if elem >= '0' and elem <= '9':
        idx2 = 1
    else:
        idx2 = 0

    if idx2 == 1:
        b.append(elem)

b = ''.join(b)

print(int(a) + int(b))