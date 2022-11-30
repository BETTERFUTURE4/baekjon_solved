T = int(input())

def fibonachi(n):
  if n <= 1:
    return n
  else:
    return fibonachi(n-2) + fibonachi(n-1)
  
print(fibonachi(T))