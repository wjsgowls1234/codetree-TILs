arr=input().split()

h=float(arr[0])
w=float(arr[1])
b = w / (h / 100)**2

print("%.1d" %b)
if b >= 25:
    print("Obesity")