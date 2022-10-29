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

N = int(input())
road = []
for _ in range(N):
    road.append(list(map(int,input().rstrip()))) # 길 등록

move = [(-1,0),(1,0),(0,-1),(0,1)] #방향 상하좌우
use_road = []
count = 2

# 갈 수 있는 길을 먼저 파악을 한다.
for i in range(N):
    for j in range(N):
        if int(road[i][j]) == 1:
            use_road.append((i,j))

for start in use_road:
    y = start[0]
    x = start[1]
    if int(road[y][x]) != 1: #이미 진행이 완료 되었다면 넘어가라
        continue
    queue = deque()
    queue.append((y,x))
    #그룹 찾기 진행
    while queue:
        y,x = queue.popleft()
        for move_y, move_x in move:
            check_x = x+ move_x
            check_y = y+ move_y
            if 0 <= check_x < N and 0 <= check_y < N: #범위에서 벗어나지 않았을 때
                if int(road[check_y][check_x]) == 1: #갈 수 있는 길이라면
                    road[check_y][check_x] = count
                    queue.append((check_y, check_x))

    count +=1 #queue가 끝나는 경우 count를 올려준다.

result_list = []
for y,x in use_road:
    result_list.append(road[y][x])

result_list.sort()

print(count-2) # 총 단지 수
for check in range(2,count):
    print(result_list.count(check))
    
