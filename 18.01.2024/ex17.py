from itertools import combinations as comb

with open("C:/Users/paush/Desktop/17.txt") as file:
  arr = [int(x[:-1]) for x in file]

cache = []

for i in comb(arr, 2):
  if ((i[0] - i[1]) % 36 == 0) and (i[0] % 13 == 0 or i[1] % 13 == 0):
   cache.append(abs(i[0] - i[1]))

print(len(cache), max(cache))