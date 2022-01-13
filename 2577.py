a = int(input())
b = int(input())
c = int(input())

count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
result = a * b * c
numbers = list(str(result))

for num in numbers:
    count[int(num)] += 1

for c in count:
    print(c)