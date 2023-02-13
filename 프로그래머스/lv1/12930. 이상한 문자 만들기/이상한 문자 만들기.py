def solution(s):
    answer = ''
    #1. 문자열을 리스트로 쪼개기
    #2. 각 문자열 홀수번을 소문자 함수, 짝수번은 대문자 함수 사용, answer 스트링에 추가
    
    for word in s.split(' '):
        for index, alp in enumerate(word):
            if index % 2 == 1:
                answer += alp.lower()
            else:
                answer += alp.upper()
        answer += ' '
        
    return answer[0: -1]