with open("C:/Users/paush/Desktop/24.txt") as file:
  file = file.read()

file = file.replace('KL', '_')
file = file.replace('LK', '_') # не учел второй возможный порядок  
file = file.split('_')
file = list(map(lambda x: len(x) + 2, file))
print(max(file))