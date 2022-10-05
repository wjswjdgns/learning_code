def solution(idx, airplane):
    visited[idx] = 1
    for road in trip_solution[idx]:
        if visited[road-1] == 0:
            airplane = solution(road-1, airplane+1)  
    return airplane

import sys
    
T = int(sys.stdin.readline()) #테스트케이스

for testcase in range(T):
    N,M = map(int, sys.stdin.readline().split()) # N : 국가 수, M : 비행기 종류
    trip_solution = [[] for _ in range(N)] # 트리 구하기
    visited = [0 for _ in range(N)]
    for _ in range(M):
        a,b = map(int, sys.stdin.readline().split()) # a와 b를 왕복하는 비행기
        
        trip_solution[a-1].append(b)
        trip_solution[b-1].append(a)

    result = solution(0,0) # 시작 country, 비행기 종류 수
    print(result)