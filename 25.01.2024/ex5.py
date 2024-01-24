def translate(n: int) -> str:
  cache = []
  while n >= 3:
    cache.append(n % 3)
    n //= 3
  cache = list(map(str, cache))
  return str(n) + ''.join(cache[:: -1])

for n in range(10**4):
  res = translate(n)
  if n % 3 != 0:
    res += translate((n % 3)*5)
  if int(res, 3) > 146: 
    print(n)
    break




