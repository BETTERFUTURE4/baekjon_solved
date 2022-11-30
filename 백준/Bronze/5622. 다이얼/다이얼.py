num = 0
for s in input():
  if ord('A') <= ord(s) <= ord('C'):
    num += 3
  elif ord('D') <= ord(s) <= ord('F'):
    num += 4
  elif ord('G') <= ord(s) <= ord('I'):
    num += 5
  elif ord('J') <= ord(s) <= ord('L'):
    num += 6
  elif ord('M') <= ord(s) <= ord('O'):
    num += 7
  elif ord('P') <= ord(s) <= ord('S'):
    num += 8
  elif ord('T') <= ord(s) <= ord('V'):
    num += 9
  elif ord('W') <= ord(s) <= ord('Z'):
    num += 10

print(num)