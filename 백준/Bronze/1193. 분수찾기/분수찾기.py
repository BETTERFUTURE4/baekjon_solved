n = int(input())
num = 0
count = 0

while num < n:
  num += count
  count +=1
  
a = 1 + (num-n)
if count % 2 == 1:#홀수
  print('%d/%d'%(count-a,a))
else:
  print('%d/%d'%(a,count-a))