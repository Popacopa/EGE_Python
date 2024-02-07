with open("C:/Users/paush/Desktop/18.txt") as file:
  matrix = [list(map(int, x[:-1].split('\t'))) for x in file]


def move(mat, x, y, s, k=0):
  s += mat[y][x] if mat[y][x] > k else 0
  k = mat[y][x] 
  if x == len(mat[0]) - 1 and y == 0: return s
  if x == len(mat[0]) - 1: return move(mat, x, y - 1, s, k)
  if y == 0: return move(mat, x + 1, y, s, k)
  if x < len(mat[0]) - 1 and y > 0: return max(move(mat, x + 1, y, s, k), move(mat, x, y - 1, s, k))


print(move(matrix, 0, 14, 0))


  






