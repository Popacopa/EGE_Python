""" from sys import setrecursionlimit
setrecursionlimit(2000) """

def summ(str):
  if len(str) == 1: return int(str)
  return int(str[-1]) + summ(str[:len(str) - 1])

cnt = 0

for n in range(3, 10**4):
  s = '5' + '2'* n
  while '52' in s or '1122' in s or '2222' in s:
    if '52' in s:
      s = s.replace('52', '1', 1)
    if '2222' in s:
      s = s.replace('2222', '5', 1)
    if '1122' in s:
      s  =s.replace('1122', '25', 1)
  if summ(s) == 88: 
    print(n)
    break
   
