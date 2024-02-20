# https://kompege.ru/variant?kim=25028275

with open("C:/Users/paush/Downloads/26_9756.txt") as file:
  file = [list(map(int, i[:-1].split(' '))) for i in file]

file.sort(key=lambda x: x[1])

#---------------------первая часть-----------------------
l1 = []
l1.append(file[0])

for i in range(1, len(file)):
  if file[i][0] >= l1[-1][1]: l1.append(file[i])

print(len(l1))
#---------------------вторая часть-----------------------
l2 = []
for i in file:
  if i[0] >= l1[-2][0]: l2.append(i)
l2.sort(key=lambda x: x[1])
print(l2[-1][1])