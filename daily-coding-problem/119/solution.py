import math

def solution(points):
    start = math.inf
    end = -math.inf

    for point in points:
        ind_start, ind_end = point

        if ind_end < start:
            start = ind_end
        if ind_start > end:
            end = ind_start

    return set([start,end])



print(solution([[0, 3], [2, 6], [3, 4], [6, 9]])) #prints {3,6}
print(solution([[0,2],[4,7],[5,6],[2,4]])) #prints {2,5}
