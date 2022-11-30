import math

def solution(fees, records):
    answer = []
    # fees : 기본시간, 기본요금, 단위시간, 단위요금
    # record 길이는 1000 이하
    # record : 시각, 차량번호, 내역
    
    # 모든 레코드 스트링 파싱
        # 시간 배열로 변환
    a = toEmptyArray(records)
    dt = dict()
    for i in getCars(a):
        dt[i] = {'IN':[],'OUT':[]}
    dt = toArray(records, dt)
    # 같은 차량 별로 값 모으기
        # 차량 별 시간 계산하기
    rs = calTime(dt, fees)
    # 계산 결과를 리스트로 반환
    # 차량 번호가 적은 차 순으로 나열
    rst = [i for i in rs.items()]
    rst.sort(key = lambda m:m[0])
    # print(rst)
    return [i[1] for i in rst]
    # return 0


def getCars(arr):
    return [a for a in arr]

def calTime(dt, fees):
    # out 모두 더한 뒤 in 빼기
    # 음수일 시 23:59로 치기
    rs = dict()
    for t in dt.keys():
        result = 0

        for out in dt[t]['OUT']:
            result += out[0] * 60 + out[1]
        for inn in dt[t]['IN']:
            result -= inn[0] * 60 + inn[1]
        if result <= 0:
            result += 23 * 60 + 59
        rs[t] = getFees(fees,result)
    return rs
        
def getFees(fees,m):
    dft = fees[0]
    dfmy = fees[1]
    t = fees[2]
    my = fees[3]
    if m <= dft:
        return dfmy
    else:
        return dfmy + my * math.ceil(((m - dft)/t))
    
def toArray(records,dt):
    for r in records:
        objs = r.split(" ")
        io = objs[2]
        dt[int(objs[1])][io].append(timeToNums(objs[0]))
    return dt
    
def toEmptyArray(records):
    answer = dict()
    for r in records:
        objs = r.split(" ")
        answer[int(objs[1])] = dict()
    return answer

def timeToNums(time):
    ts = time.split(":")
    return [int(ts[0]), int(ts[1])]