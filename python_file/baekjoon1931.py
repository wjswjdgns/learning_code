# 고려해야 하는점
# 시작과 끝이 너무 길 경우 많은 회의를 할 수 없기 때문에 끝나는 시간 기준으로 오름차순 정렬 필요
# 2,2 1,2의 경우 1로 받아들여 질 수 있기 때문에 시작하는 시간의 오름차순 필요

import sys
input = sys.stdin.readline
N = int(input())
time = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x:(x[1], x[0])) #끝나는 시간 기준을 오름차순 이후에 시작하는 시간 오름차순 정렬

count = 0
end = 0
for s,e in time:
    if s >= end:
        count += 1
        end = e
        
print(count)