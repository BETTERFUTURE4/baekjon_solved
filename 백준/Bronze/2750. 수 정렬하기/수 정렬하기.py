N = int(input())
arr = list()
for __ in range(N):
  n = int(input())#1)수를 받음
  # 2)담겨있는 배열의 수들과 차례로 비교
  for i in range(len(arr)):
    if n <= arr[i]:
      #배열수 이전에 값 넣기
      arr = arr[:i] + [n] + arr[i:]
      break
  else: 
    arr.append(n)

for i in arr: print(i) 