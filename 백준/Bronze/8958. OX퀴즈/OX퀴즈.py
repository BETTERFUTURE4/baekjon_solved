import sys

n = int(input())

for idx in range(n):
  count = 0
  score = 0
  
  arr = list(sys.stdin.readline().rstrip())
  
  for a in arr:
    if a == 'O':
      count += 1
      score += count
    elif a == 'X' :
      count = 0
      
  print(score)