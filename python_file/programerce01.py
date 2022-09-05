# 0은 빈칸을 의미 이걸 몰랐네; 
board =[[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves =[1, 5, 3, 5, 1, 2, 1, 4] #인덱스 값 가로 값은 동일하게 유지


def solution(board, moves):
    answer = 0
    play_count = len(moves)
    stack_list = [None] * play_count #빈 스택 완성
    stack_count = 0

    for i in range(play_count): #게임 시작
        check_count = 0 
        check = True
        
        #빈칸 확인
        while check:
            if check_count > len(board)-1: #세로 길이가 넘어가게 된다면
                    check = False
                    break

            if board[check_count][moves[i]-1] == 0: #해당 구역이 0(빈칸) 이였을 경우 더 깊이 내려간다
                check_count +=1
            else:
                value = board[check_count][moves[i]-1]
                board[check_count][moves[i]-1] = 0 #꺼내기
                break #서칭 종료
        
        if check == False: #해당 구역에는 빈공간으로 아무것도 하지 않고 넘어간다
            continue
        
        else:
            if stack_list[stack_count-1] == value: #pop
                answer +=2
                stack_count -= 1
                stack_list[stack_count] = None
                continue

            stack_list[stack_count] = value #push
            stack_count+=1

    return answer


print(solution(board, moves))


#선형구조로 만들어야 하는가 --> 일단 만들고 개선 해보도록 하자


