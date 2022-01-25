arr = int(input())
remains = []
for n in arr:
  a = n % 42
  if a not in remains:
    remains += [a]