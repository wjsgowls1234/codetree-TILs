str = input()
sum_val = 0

for elem in str:
    if elem.isdigit():
        elem = int(elem)
        sum_val += elem
print(sum_val)