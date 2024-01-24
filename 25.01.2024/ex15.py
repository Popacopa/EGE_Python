

for a in range(100):
  cache = []
  for x in range(100):
    for y in range(100):
      cache.append((x * y < 100) or (y >= a) or (x > a))
  if all(cache):
    print(a)