arr = [-1 for __ in range(26)]

word = input()
for i, w in enumerate(word):
  if arr[ord(w)-97] == -1:
    arr[ord(w)-97] = i

print(*arr)