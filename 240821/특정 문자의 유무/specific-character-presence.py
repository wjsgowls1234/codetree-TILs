string = input()

length = len(string)
exists1 = False
exists2 = False

for i in range(length - 1):
    if string[i] == 'e' and string[i + 1] == 'e':
        exists1 = True
    if string[i] == 'a' and string[i + 1] == 'b':
        exists2 = True

if exists1 == True or exists2 == True:
    print("Yes", end=" ")
if exists1 == False or exists2 == False:
    print("No")