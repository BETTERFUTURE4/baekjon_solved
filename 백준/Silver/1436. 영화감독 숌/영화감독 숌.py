N = int(input())

i = 1
num = 0
while True:
  if '666' in str(num):
    if i == N: 
      break
    else:
      i += 1
  num += 1
  
print(num)