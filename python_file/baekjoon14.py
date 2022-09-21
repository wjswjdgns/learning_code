# 팩도리얼 만들기

def solution(base):
    if base <= 1:
        return 1
    return base * solution(base-1)

N = int(input())
print(solution(N))
