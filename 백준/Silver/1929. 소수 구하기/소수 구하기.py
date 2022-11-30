m, n = map(int, input().split())
prime = [False,False] + [True]* (n-1)#0,1은 False처리

for i in range(2,int(n**0.5)+1):
  if prime[i] == True: # i가 소수인 경우 
    for k in range(2*i, n+1, i): #i이후 i의 배수들(k)을 False 판정
      prime[k] = False;

for i in range(m,n+1):
  if prime[i]:
    print(i)