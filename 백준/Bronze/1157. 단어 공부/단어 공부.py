arr = [0 for __ in range(26)]

# 단어 받기
word = input().lower()
# 각 문자별로, 해당 문자의 배열 부분의 값+1
for w in word:
  arr[ord(w)-97] += 1
# 가장 숫자가 높은 인덱스 숫자 찾기
if arr.count(max(arr))!= 1:# 해당 인덱스가 여러개면 ?, 한개면 chr()
  print('?')
else:
  print(chr(arr.index(max(arr)) + 65))