from collections import deque

def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    result = {}
    time = 0
    
    while progresses:
        p = progresses.popleft()
        s = speeds.popleft()
        if p + time*s >= 100:
            if time in result:
                result[time] += 1
            else:
                result[time] = 1            
        else:
            progresses.appendleft(p)
            speeds.appendleft(s)
            time += 1
    
    return list(result.values())