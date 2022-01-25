a = int(input())
b = int(input())
c = int(input())

res = a * b * c
cnt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while res != 0:
    n = res % 10
    res //= 10
    cnt[n] += 1

for item in cnt:
    print(item)