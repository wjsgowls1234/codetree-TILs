arr = list(map(int, input().split()))
max_value = 1
min_value = 1000

for elem in arr:
    if elem < 500:
        if elem > max_value:
            max_value = elem
    elif elem > 500:
        if elem < min_value:
            min_value = elem
print(max_value, min_value)