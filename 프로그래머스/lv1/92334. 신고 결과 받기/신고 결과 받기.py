def solution(id_list, report, k):
    answer = [0] * len(id_list)
    userReport = {x : [] for x in id_list}
    
# 레포트 마다 
    for rp in set(report):
# 정지 회수 추가, 그 유저가 신고한 유저목록에 추가      
        userReport[rp.split()[1]].append(rp.split()[0])

# 정지회수가 k를 넘은 유저 리스트 만들기
    stoped = [bad for bad in userReport.keys() if len(userReport[bad]) >= k]
    
    for rp in set(report):
        if len(userReport[rp.split()[1]]) >= k:
            answer[id_list.index(rp.split()[0])] += 1
    
    return answer
            