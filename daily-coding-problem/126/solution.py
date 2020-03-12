def solution(list,k):
    rotate = k % len(list)

    return list[rotate:] + list[:rotate]



print(solution2([1,2,3,4,5,6],2))
print(solution2([1,2,3,4,5,6],9))

