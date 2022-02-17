numeric = {
    '-': 0,
    '\\': 1,
    '(': 2,
    '@': 3,
    '?': 4,
    '>': 5,
    '&': 6,
    '%': 7,
    '/': -1
}

while True:
    puts = input()
    if puts == '#': break
    sums = 0
    for i in range(len(puts)):
        sums += numeric[puts[i]] * (8**(len(puts)-i-1))
    print(sums)