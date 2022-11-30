num = set(range(1,10001))
create = set()

for i in num:
  for j in str(i):
    i += int(j)
  create.add(i)
  
self_num = sorted(num - create)
for i in self_num:
  print(i)