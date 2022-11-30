import sys
sys.setrecursionlimit(10 ** 6)

def star(n):
  if n == 1:
    return ['*']

  arr = star(n//3)
  new_arr = list()
  for i in arr:
    new_arr.append(i*3)#1/3
  for i in arr:
    new_arr.append(i + ' '*(n//3) + i)#2/3
  for i in arr:
    new_arr.append(i*3)#3/3
  
  return new_arr

T = int(sys.stdin.readline().rstrip())

print('\n'.join(star(T)))