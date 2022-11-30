def hashOfGenres(x):
    return float(str(x[1])+ '.' + str(20000-x[0]))

def findSortedIndexs(genres, plays, genre):
    arr = []
    for i,g in enumerate(genres):
        if g == genre:
            arr.append([i, plays[i]])
    return sorted(arr, key=lambda x : hashOfGenres(x), reverse=True)

def write_count_sum(arr):
    return sum([a[1] for a in arr])


def solution(genres, plays):
    dicts = [[genre, findSortedIndexs(genres, plays, genre)] for genre in set(genres)]
    dicts = sorted(dicts, key=lambda x : write_count_sum(x[1]),reverse=True)
    arr = []
    for d in dicts:
        for count in d[1][:min(genres.count(d[0]),2)]:
            arr.append(count[0])
    return arr