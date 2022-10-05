# 문제
#그래프가 주어졌을 때, 그 그래프의 최소 스패닝 트리를 구하는 프로그램을 작성하시오.
#최소 스패닝 트리는, 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리를 말한다.

#입력

"""
첫째 줄에 정점의 개수 V(1 ≤ V ≤ 10,000)와 간선의 개수 E(1 ≤ E ≤ 100,000)가 주어진다. 
다음 E개의 줄에는 각 간선에 대한 정보를 나타내는 세 정수 A, B, C가 주어진다. 
이는 A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있다는 의미이다. C는 음수일 수도 있으며, 절댓값이 1,000,000을 넘지 않는다.

그래프의 정점은 1번부터 V번까지 번호가 매겨져 있고, 임의의 두 정점 사이에 경로가 있다. 
최소 스패닝 트리의 가중치가 -2,147,483,648보다 크거나 같고, 2,147,483,647보다 작거나 같은 데이터만 입력으로 주어진다.
"""

# 크루스칼 알고리즘 사용
# find 과정은 연결리스트로 확인하는 작업
# 

import sys
input = sys.stdin.readline

def find(value):
    if value == parent[value]: # 노드 번호와 parent 값이 같다면
        return value # 루트 값 확인
    parent[value] = find(parent[value]) # 같지 않을 경우 부모를 찾아서 이동
    return parent[value]

def union(a,b):
    rootA = find(a) # a의 루트 노드를 찾기
    rootB = find(b) # b의 루트 노드를 찾기

    if rootA != rootB:
        parent[rootB] = rootA #a의 루트 노드를 b의 루트 노드에 붙인다.
    
    
V,E = map(int, input().split()) # V 정점의 개수,  E 간선의 개수
Edge = []

for _ in range(E):
    A,B,C = map(int, input().split()) #A번 정점과 B번 정점이 가중치 C로 연결
    Edge.append((C,A,B))

Edge.sort(key=lambda x: x[0]) # 가중치 기준으로 정렬
parent = list(range(V+1))

sum = 0
for c,a,b in Edge:
    if find(a) != find(b):
        union(a,b)
        sum+= c

print(sum)