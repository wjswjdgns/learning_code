import sys
import heapq #최댓값 최솟값을 찾는 연산에 특화된 완전 이진트리 (우선순위 큐 : 최소 힙)
input = sys.stdin.readline
    
INF = int(1e9) # 무한대 값 지정
V,E = map(int, input().split()) #정점의 개수, 간선의 개수
K = int(input()) # 시작 점
value_list = [[] for _ in range(V+1)]
distance = [INF] * (V+1)

def solution(start):
    heap = []
    distance[start] = 0 #처음 시작 값을 0으로
    heapq.heappush(heap, (0, start))
    
    while heap: #어느곳으로 갈 수 없는 경우가 나올 경우 루트 탈출
        weight, node = heapq.heappop(heap) #가장 짧은 노드 가져오기
        
        if distance[node] < weight: #등록된 값보다 가중치가 더 클 경우 넘어간다.
            continue
        
        # 연결된 노드를 거쳐 지나가는 최단 경로 만들기
        for i in value_list[node]:
            cost = weight + i[0] #누적 가중치 // 0부터 시작해서 순차적으로 지나온 가중치를 더한다
            
            # 현재보다 최단 경로일 경우 갱신
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(heap, (cost, i[1]))

for _ in range(E):
    u,v,w = map(int, input().split())
    value_list[u].append((w,v))


solution(K)
 
for i in range(1,V+1): #정점의 개수 만큼 출력
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])