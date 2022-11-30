N = int(input())
arr = list()

for i in range(N):
  height, weight = map(int,input().split())
  arr.append([height,weight])

rate = list(range(N))

for me in range(N):
  max_count = 1
  for i in range(N):
    if arr[me][0] < arr[i][0] and arr[me][1] < arr[i][1]:
      max_count += 1
  rate[me] = str(max_count)

print(' '.join(rate))