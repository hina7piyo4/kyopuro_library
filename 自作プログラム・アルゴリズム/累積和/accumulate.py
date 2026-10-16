import itertools

l = [1, 2, 3, 4, 5, 6]
l = list(itertools.accumulate(l))
print(l)