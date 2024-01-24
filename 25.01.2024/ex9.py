from itertools import permutations as p 


def sr(arg: iter) -> float:
  return sum(arg) / len(arg)

with open("C:/Users/paush/Desktop/9.txt") as file:
  file = [list(map(int, x[:-1].split('\t'))) for x in file]


cnt = 0

for i in file:
  if any((x[0] == x[1] == x[2] == x[3] != x[4] != x[5] != x[6]) and (sr(x[:4]) < sr(x)) for x in p(i)):
    cnt += 1

print(cnt)