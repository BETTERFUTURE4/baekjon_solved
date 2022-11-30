def cold(a):
  arr=list()
  for i in str(a):# a 문자전환 후 반복문
    arr.append(int(i))# 숫자화, 리스트에 담기
  # 끝과 중간값 비교
  num = arr[0]+arr[len(arr)-1]
  for i in range(1, int(len(arr)/2)+1):
    if num != arr[i]+arr[len(arr)-i-1]:
      return False
  return True

n = int(input())
count = 0
for i in range(1,n+1):
  if cold(i):
    count += 1
print(count)