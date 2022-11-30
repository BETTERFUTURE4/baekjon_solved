import sys

n = int(input())

for i in range(1,n+1):
  a,b = map(int, sys.stdin.readline().rstrip().split())
  print("Case #%d: %d + %d = %d" % (i, a, b, a+b))