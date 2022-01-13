flag = True
while flag:
    puts = input()
    arr = puts.split()
    a = int(arr[0])
    b = int(arr[1])
    c = a+b
    if c == 0:
        flag = False
    else:
        print(c)