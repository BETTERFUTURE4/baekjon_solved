n = int(input())

r = 31
m = 1234567891

str = input()
result = 0
idx = 0
for s in str:
    result += (ord(s)-96)*(r**idx)
    idx+=1

print(result)