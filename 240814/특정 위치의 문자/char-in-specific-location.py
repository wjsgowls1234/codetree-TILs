arr=['L','E','B','R','O','S']

word=input()

if word not in arr:
    print("None")
else:
    print(arr.index(word))