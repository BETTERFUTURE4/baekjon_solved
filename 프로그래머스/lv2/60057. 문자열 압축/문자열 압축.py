def solution(s):
    answer = len(s)
    max_unit = int(len(s)//2)

    # 루트 개수만큼 반복
    for unit in range(1, max_unit+1):
        str_list = list()
        # 유닛 단위로 문자 자르기
        idx = 0
        for i in range(len(s)//(unit)):
            idx = unit*i
            obj = s[idx : idx+unit]

            if str_list != [] and obj == str_list[-1]:
                str_list[-2] += 1
            else:
                str_list.append(1)
                str_list.append(obj)

        str_join = ""
        for i in str_list:
            if i != 1:
                str_join += str(i) 
        str_join += s[idx+unit:]
        
        answer = min(answer,len(str_join))
    return answer