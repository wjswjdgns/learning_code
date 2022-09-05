priorities = [1, 1, 9, 1, 1, 1]
location = 0

def solution(priorities, location):
    answer = 0
    len_value = len(priorities)
    max_value = max(priorities)
    index_Queue = [i for i in range(len_value)]

    while True:
        if priorities[0] == max_value:
            answer += 1
            if index_Queue[0] == location:
                break
            #인쇄 진행
            del priorities[0]
            del index_Queue[0]
            max_value = max(priorities) #최댓값 재설정

        else:
            priorities.append(priorities[0])
            index_Queue.append(index_Queue[0])
            del priorities[0]
            del index_Queue[0]
            
    # 2개의 큐로 돌린다?
    # return = 인쇄를 별도로 잡아야 한다.
    return answer

print(solution(priorities, location))