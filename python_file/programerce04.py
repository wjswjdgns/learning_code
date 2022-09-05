n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
from collections import deque
def BFS(one, list):
    pass

def solution(n, edge):
    answer = 0
    value_list = [[] for _ in range(n)]
    visited = [False for _ in range(n)]
    node_count = [[] for _ in range(n)]

    BFS_queue = deque()
    BFS_queue.append(1)
    count = 1

    for a,b in edge:
        value_list[a-1].append(b)
        value_list[b-1].append(a)
    
    while visited:
        value = BFS_queue.popleft
        for pop_value in value_list[value-1]:
            if visited[pop_value-1] == False:
                visited[pop_value-1] = True
                node_count[pop_value-1] = count
                BFS_queue.append(pop_value)
        count+=1
    return answer


print(solution(n,vertex))