from itertools import permutations

file = open("C:/Users/paush/Desktop/9.txt")
file = [map(int, n[:-1].split('\t')) for n in file]

cnt = 0

for i in file:
  if all(n[0] + n[1] > n[2] for n in permutations(i, 3)): cnt += 1

print(cnt)