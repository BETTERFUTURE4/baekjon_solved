n = int(input())
count = n
for i in range(n):
  str = input()

  if len(str) >= 3:
    i = 2
    while i <= len(str) - 1:
      if str[i-1] != str[i] and str[:i-1].count(str[i]) >= 1:# 해당글자 와 연속안된 앞에 글자 있으면 false
        count -= 1
        break
      elif str[i-1] == str[i]:# 해당글자 바로뒤에 있으면 그 글자 빼고 str 다시저장
        str = str[:i] + str[i+1:]
        i -= 1
      i += 1
    
print(count)