N,M = map(int, input().split()) # M =행 N= 열
value_list = []
min_count = 10000
for i in range(N):
    value_list.append(input())

#범위 설정 (모든 경우의 수)
for col in range(N-7): #세로 기준
    for row in range(M-7): #가로 기준
        b_count = 0 #black기준
        w_count = 0 #white기준
        
        for c in range(8): #기준에 맞게 8*8 생성 (세로)
            for r in range(8):  #기준에 맞게 8*8 생성 (가로)
                
                if ((c+col)+(r+row)) %2 == 0: 
                    if value_list[c+col][r+row] != 'B': #처음 시작이 블랙인 경우
                        b_count += 1
                    if value_list[c+col][r+row] != 'W': #처음 시작이 화이트인 경우
                        w_count +=1
                else:
                    if value_list[c+col][r+row] != 'W': #두번째가 화이트인 경우 (처음 시작이 블랙인 경우)
                        b_count += 1
                    if value_list[c+col][r+row] != 'B': #두번째가 블랙인 경우 (처음 시작이 화이트인 경우)
                        w_count += 1
        min_count = min(min_count, w_count, b_count)
            

print(min_count)
#해당 범위 안에 고쳐야 할 수 확인 (흰색, 검은색)