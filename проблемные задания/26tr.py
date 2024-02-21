with open("C:/Users/paush/OneDrive/Рабочий стол/26_59821.txt") as file:
  file = [list(map(int, i[:-1].split('\t'))) for i in file]

right = []
left = []
cache = []

for i in file:
  if min(i[:2]) == i[0] and min(i[:2]) not in cache: 
    left.append(i)
    cache.append(min(i[:2]))
  if min(i[:2]) == i[1] and min(i[:2]) not in cache:
    right.insert(0, i)
    cache.append(min(i[:2]))

print(left[-1][2])
