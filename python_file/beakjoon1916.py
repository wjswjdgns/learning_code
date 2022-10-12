import sys
import heapq #최댓값 최솟값을 찾는 연산에 특화된 완전 이진트리 (우선순위 큐 : 최소 힙)
input = sys.stdin.readline

def solution(start, end):
    heap = []
    heapq.heappush(heap, (0, start)) #시작지점을 힙에 저장
    distance[start] = 0 #첫 시작 지점 0으로 시작
    
    while heap: #더 이상 갈 곳이 없을 때 while 문 탈출
       h_cost, h_start = heapq.heappop(heap)
       
       if distance[h_start] < h_cost: #등록된 값보다 가중치가 더 클 경우 넘어간다. (해당 코드 제외 시 시간 초과)
            continue
        
       for i in graph[h_start]:
           sum_cost = h_cost + i[1] #가중치 합산
           
           if sum_cost < distance[i[0]]:
               distance[i[0]] = sum_cost
               heapq.heappush(heap, (sum_cost, i[0]))
               
    return distance[end]
    
INF = int(1e9) # 무한대 값 지정
N = int(input()) #도시
M = int(input()) #버스

graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    
start, end = map(int, input().split())

print(solution(start, end))