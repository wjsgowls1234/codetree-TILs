string = input().split()

a = string[0]
b = string[1]

if len(a) > len(b):
    print(a, len(a))
elif len(a) < len(b):
    print(b, len(b))
else:
    print("same")