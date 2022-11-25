# 백준 - 바이러스
from collections import deque

N = int(input()) # 컴퓨터의 수
count = int(input())
graph = [[] for _ in range(N+1)]
visited = [ 0 for _ in range(N+1)]

for i in range(count):
    start,end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

def solution(start_node):
    queue = deque()
    queue.append(start_node)
    visited[start_node] = 1
    result = 0
    
    while queue: #q가 없어 질때까지 반복해라
        value = queue.popleft()

        for num in graph[value]:
            if visited[num] == 1:
                continue
            queue.append(num)
            visited[num] = 1
            result += 1
    
    return result
print(solution(1))

