dis_dic ={'2':['135','468','790','#*'],
          '5':['2468','13790','#*'],
          '8':['5790','246#*','13'],
          '0':['8#*','579','246','13']
          }

def distance(now,next):
  dt = -1
  d_arr = dis_dic[str(next)]
  for i in range(len(d_arr)):
    if str(now) in d_arr[i]:
      dt = i
      break
  return dt

def solution(numbers, hand):
  answer = ''
  left = [1,4,7]
  right = [3,6,9]
  
  th = {'L':'*','R':'#'}
  
  for n in numbers:
    # 147, 369 세팅
    if n in left:
      answer += 'L'
      th['L'] = n
    elif n in right:
      answer += 'R'
      th['R'] = n

    # 2580 세팅
    else:
      # 거리계산
      ld = distance(th['L'],n)
      rd = distance(th['R'],n)
      # 두 거리가 같으면: 잡이에 따라
      if ld == rd:
        thumb = hand[0].upper()
        answer += thumb
        th[thumb] = n
        
      # 같지않으면: 더 가까운 거 사용
      else:
        if ld < rd:
          answer += 'L'
          th['L'] = n
        else:
          answer += 'R'
          th['R'] = n

  return answer