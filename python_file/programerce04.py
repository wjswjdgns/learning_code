n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
from collections import deque

def solution(n, edge):
    answer = 0
    value_list = [[] for _ in range(n)] #그래프를 위한 리스트
    visited = [False for _ in range(n)] #방문 기록
    node_count = [0 for _ in range(n)]  #BFS 단계 등록을 위한 리스트
    
    BFS_queue = deque() #BFS를 위한 큐 선언
    BFS_queue.append(1) #1로 초기 등록
    level =  1 # 1 이후는 거리가 1이여서 1부터 시작
    
    #그래프 만들기
    for a,b in edge:
        value_list[a-1].append(b)
        value_list[b-1].append(a)
        
    #BFS
    while BFS_queue:
        for _ in range(len(BFS_queue)): #BFS 단계가 끝나는 순간을 확인하는 for 문
            value = BFS_queue.popleft()
            for pop_value in value_list[value-1]:
                if visited[pop_value-1] == False:
                    visited[pop_value-1] = True
                    BFS_queue.append(pop_value)
                    node_count[pop_value-1] = level
        level += 1 
        
    answer = node_count[1:].count(max(node_count)) #1부터 시작하기 때문에 1을 제외하고 가장 멀리떨어진 노드들을 count로 확인
    return answer


print(solution(n,vertex))