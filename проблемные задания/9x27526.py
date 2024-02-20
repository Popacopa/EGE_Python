from statistics import mean

with open("C:/Users/paush/OneDrive/Рабочий стол/9.txt") as file:
  file = [list(map(float, i[:-1].split('\t'))) for i in file]

cnt = 0

for i in file:
  maximum = max(i) / 2
  sr = round(mean(i), 1) / 2
  for n in i:
    if sr < n < maximum: cnt += 1

print(cnt)


