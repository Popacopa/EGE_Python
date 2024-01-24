from itertools import combinations as comb

with open("C:/Users/paush/Desktop/17.txt") as file:
  file = [int(i) for i in file]

cache = []

for i in comb(file, 2):
  if (i[0] + i[1]) % 10 == 0:
    cache.append(i[0] + i[1])

print(len(cache), max(cache))