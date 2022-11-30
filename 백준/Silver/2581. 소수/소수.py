m = int(input())
n = int(input())

prime = [False,False] + [True] * (n-1)

for i in range(2,int(n**0.5)+1):
  if prime[i]:
    for k in range(i*2,n+1, i):
      prime[k] = False

arr = list()
for i in range(m,n+1):
  if prime[i]:
    arr.append(i)

if len(arr) != 0:
  print(sum(arr))
  print(min(arr))
else: print(-1)