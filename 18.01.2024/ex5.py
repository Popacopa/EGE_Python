
cnt = 0

for n in range(100, 1000):
  cache = []
  for i in range(len(str(n)) - 1):
    cache.append(int(str(n)[i]) + int(str(n)[i + 1]))
    cache.sort()  #забыл про порядок возрастания
  if cache == [12, 16]:
    cnt += 1

print(cnt)