string = ''

while True:
    
    if string == 'END':
        break

    string = input()

    if string == 'END':
        continue

    print(string[::-1])