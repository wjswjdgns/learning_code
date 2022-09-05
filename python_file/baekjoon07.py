from collections import deque
def DFS(start):
    visited01[start] = True
    print(start+1, end=" ")
    for i in value_list[start]:
        if visited01[i-1] != True:
            DFS(i-1)
            
def BFS(start):
    child = deque()
    child.append(start+1) #값이기에 +1
    road = child.popleft()
    
    while road <= N: #이후 큐에 있는 값으로 BFS 방문 시작
        road = child.popleft()
        print(road, end=" ")
        for j in value_list[road-1]:
            child.append(j)

N,M,V = map(int,input().split())
value_list = [[] for _ in range(N)]
visited01 = [False for _ in range(N)]

for _ in range(M):
    a,b = map(int, input().split())
    value_list[a-1].append(b)
    value_list[b-1].append(a)

for i in range(N): #정렬
    value_list[i].sort() #작은 숫자부터 가져오기 위해 정렬

DFS(V-1)
print()
BFS(V-1)


