from itertools import product as p

cache = []

for n in p('ТИМОФЕЙ', repeat=5):
  if n.count('Т') >= 1 and n.count('Й') <= 1:
    cache.append(n)

print(len(cache))



