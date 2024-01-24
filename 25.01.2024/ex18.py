with open("C:/Users/paush/Desktop/18.txt") as file:
  file = [list(map(int, x[:-1].split('\t'))) for x in file]


def move(s, x, y, matrix):
  s += matrix[x][y]
  if x == len(matrix) - 1 and y == len(matrix) - 1: return s
  if x == len(matrix) - 1: return  move(s, x, y + 1, matrix)
  if y == len(matrix) - 1: return  move(s, x + 1, y, matrix)
  if x < len(matrix) - 1 and y < len(matrix) - 1: 
    return min(move(s, x, y + 1, matrix), move(s, x + 1, y, matrix))
  

print(move(0, 0, 0, file))