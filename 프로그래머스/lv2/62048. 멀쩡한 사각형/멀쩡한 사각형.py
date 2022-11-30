def factorization(s,l): 
  factor = 1
  i = 2
  while i <= s:
    if s % i == 0 and l % i == 0:
      factor *= i
      s /= i
      l /= i
    else:
      i += 1
  return int(s),int(l),int(factor)

def solution(w,h):
  s, l, factor = factorization(w,h)
  lean = (s/l)
  count = lean * l + l - 1
  return int(w*h-(count * factor))

print(solution(8,12))