with open("C:/Users/paush/OneDrive/Рабочий стол/9.txt", 'r') as file:
  file = [list(map(int, i[:-1].split('\t'))) for i in file]

cnt = 0

for i in file:
  cache = [i.count(n) for n in i]
  if cache.count(2) == 4 and cache.count(1) == 2:
    cache = [(n, i.count(n)) for n in i]
    sumofone = []
    sumofrep = []
    for n in cache:
      if n[1] == 2 and n[0] not in sumofrep: sumofrep.append(n[0])
      if n[1] == 1 and n[0] not in sumofone: sumofone.append(n[0])
    if sum(sumofrep) < sum(sumofone):
      cnt += 1

print(cnt)