num = int(input())
temp = num
count = 0

while True:
  count += 1
  
  ten = int(temp / 10)
  one = temp % 10
  
  temp = one * 10 + (ten+one)%10
  
  if temp == num:
    break

print(count)