
for a in range(90):
  cache = [((x % 3 != 0) or (x % 5 != 0)) or (x + a >= 90) for x in range(1, 1000)]
  if all(cache): 
    print(a)
    break

