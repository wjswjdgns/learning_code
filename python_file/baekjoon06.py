from collections import deque
N,M = map(int,input().split())
value_list = []
for _ in range(N):
    value_list.append(list(map(int, input())))

road_queue = deque() # 스택
road_queue.append([0,0])
move = [(-1,0),(1,0),(0,-1),(0,1)] # 상하좌우 좌표 설정
level = 0 #몇번의 길을 거치게 되었는지 (결과값)
roop = True

while roop: #스택이 끝날때까지 진행 ~ 수정 필요 최단거리로 진행하고 있기 때문에 종료 조건을 바꿔야 한다.!
    
    for _ in range(len(road_queue)): #현재 road_queue 길이 만큼 반복
        y,x = road_queue.popleft()
        if y == N-1 and x == M-1: # 조건 성립 안됨
            roop = False
            break

        for a,b in move:
            move_y = y+a
            move_x = x+b
            # 범위를 벗어나지 않고, 갈 수 있는 길이였을 때 추가
            if 0 <= move_x < M and 0 <= move_y < N:
                if value_list[move_y][move_x] == 1:
                    road_queue.append((move_y,move_x)) #갈 수 있는 길을 큐에 넣는다.
                    value_list[y][x] +=1 #지나갔다는 것을 표시
    level+=1
    
print(level)


#한번의 루트가 완료가 되면 리셋         

#좌우상하 확인 (1인 구간 찾기)

#스택에 담기 

#[N,M]이 체크 했을 떄 종료


