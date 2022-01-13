h, m, s = map(int, input().split())
delta = int(input())
s = s + delta
m = m + s // 60
h = h + m // 60
s = s % 60
m = m % 60
h = h % 24
print(h, m, s)