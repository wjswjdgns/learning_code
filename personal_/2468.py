# 안전 영역

# 비가 왔을 때 물에 잠기는 영역을 확인 (BFS)
# 영역을 확인 하는 코드
# 전체가 잠겼을 경우 반복 종료

from collections import deque
N = int(input())
value_list = []
max_num = 0 #최대 높이 확인
result = 0 #안전영역
move = [(-1,0),(1,0),(0,-1),(0,1)] # 상하좌우
count = 0

for _ in range(N): #값 추가
    area = list(map(int, input().split()))
    max_num = max(max_num, max(area))
    value_list.append(area)

def rain_bfs(rain_y,rain_x,rain_value):
    queue = deque()
    queue.append((rain_y,rain_x))
    visited[rain_y][rain_x] = 1
    while queue:
        def_y, def_x = queue.popleft()
        
        for m_y, m_x in move:
            trans_y = def_y + m_y
            trans_x = def_x + m_x
            if (trans_y < 0 or trans_y >= N) or (trans_x < 0 or trans_x >= N): # 영역 벗어 났을 경우 패스
                continue
            if visited[trans_y][trans_x] == 1:
                continue
            if value_list[trans_y][trans_x] > rain_value:
                visited[trans_y][trans_x] = 1
                queue.append((trans_y, trans_x))

# 비 영역 + 안전 구역 확인
for rain in range(max_num): # 어떤 지역도 잠기지 않을 수 있기 때문에 최대 높이 이전까지 진행한다.
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if visited[y][x] == 1:
                continue
            if rain < value_list[y][x]:
                rain_bfs(y,x,rain)
                count += 1
    result = max(result, count)
    count = 0

print(result)
