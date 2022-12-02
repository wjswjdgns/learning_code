# 주어진 숫자에 이어진 집의 개수를 확인해야 한다.
# 각 집의 개수를 확인 후 오름차순 한다음 그것을 출력
# 상하좌우 이론을 그대로 사용

# for 문을 통해 값 증가 필요 (집 개수 확인 max값 -1 이 집의 갯수)
# count 필요 (각 숫자의 갯수 확인)
# 어느 쪽도 1이 아닐 경우 또 다른 1을 찾아서 진행 ? 

# while 문 필요 (종료 시 값 증가)
# 큐 필요
# 1을 스캔하면서 확인


from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, y, x):
    n = len(graph)
    queue = deque()
    queue.append((y,x))
    graph[y][x] = 0 #이미 지나온 곳을 0으로 표시
    count = 1 # 총 갯수 표시

    #반복하며 
    while queue:
        y,x = queue.popleft() #값 꺼내기
        
        for m_y, m_x in move:
            ny = y + m_y #y좌표로 이동 
            nx = x + m_x #x좌표로 이동

            #경로에 벗어 났을 경우 넘어간다. 
            if (ny < 0 or ny >= N) or (nx < 0 or nx >=N):
                continue
            
            # 갈 수 있는 길이라면
            if graph[ny][nx] == 1: 
                graph[ny][nx] = 0 #이미 갔다는 표시하고
                queue.append((ny, nx)) #큐에 담고
                count += 1 #카운트를 늘린다.
  
    return count

value = []
N = int(input()) # 정사각형 크기

for i in range(N): #N개의 자료
    value.append(list(map(int, input().rstrip()))) #앞쪽에 0이 있기 때문에

move = [(-1,0),(1,0),(0,-1),(0,1)] #상하좌우 설정
cnf = []
#bfs 와 dfs로 풀기

for i in range(N):
    for j in range(N):
        if value[i][j] == 1:
            bfs(value, i, j)

# 오름 차순을 위해 정렬
cnf.sort()

# 정답 출력

print(len(cnf))
for result in cnf:
    print(result)