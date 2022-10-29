#BFS 연습 순열 싸이클
#그래프를 계속해서 타고 건너가는 개념을 BFS, DFS로 생각을 하면 된다.

import sys
input = sys.stdin.readline

T = int(input())

for testcase in range(T):
    N = int(input())
    value_list = list(map(int, input().split())) # 순열
    
    graph = [[] for _ in range(N)] #그래프 만들기
    visited = [0 for _ in range(N)] #방문 기록 확인
    count = 0 #사이클 수 확인

    for idx,value in enumerate(value_list):
        graph[idx].append(value)

    for i in range(N):
        if visited[i] == 1:
            continue
        
        start_node = graph[i][0] # 시작 숫자 방문
        visited[start_node-1] = 1
        tmp = start_node

        while True:
            start_node = graph[start_node-1][0] # 새로 갱신

            if tmp == start_node:
                count+=1 #while 문이 끝나는 순간 count 증가
                break

            visited[start_node-1] = 1 # 방문표시

    print(count)