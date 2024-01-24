def summ(str: str) -> int:
  if len(str) == 1: return int(str)
  return int(str[-1]) + summ(str[:len(str) - 1])


def is_simple(int: int) -> bool:
  for i in range(2, int // 2):
    if int % i == 0: 
      return False
  return True

for n in range(1, 40):
  s = '0' + (40 - n)*'1' + (n)*'2'
  result = summ(s)
  while '01' in s or '02' in s:
    if '02' in s: s = s.replace('02', '1110', 1)
    if '01' in s: s = s.replace('01', '220', 1)
  if is_simple(summ(s)): 
    print(result)
    break