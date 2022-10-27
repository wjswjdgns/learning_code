# 

n = 13
lost = [1, 2, 5, 6, 10, 12, 13]
reserve = [2, 3, 4, 5, 7, 8, 9, 10, 11, 12]

def solution(n,lost, reserve):
    answer = 0
    remains = [1] * n
    
    # 순차적으로 진행 + 잃어버린 사람부터 체크를 했기 때문에 여분용을 가지고 있지만
    # 가지고 있지 않다고 코드상으로 판단되어 넘겨주게 되고 이후 해당되는 번호가 왔을때
    # 하나를 추가 해줌으로써 여분용이 없지만 여분용이 있다고 판단하게 되고
    # 이후부터는 코드가 꼬이기 시작
    
    # 여벌용은 가지고 있는데 도난당한 사람 체크
    reserve_l = list(set(reserve) - set(lost))
    lost_l = list(set(lost) - set(reserve))
    
    # 잊어버린 사람 체크
    for i in lost_l:
        remains[i-1] -= 1
    
    # 여분용 체크 및 양 옆 빌려주기
    for i in reserve_l:
        remains_person = i-1
        remains[remains_person] += 1
        f_lost_person = remains_person - 1
        e_lost_person = remains_person + 1
        
        if f_lost_person >= 0:
            if remains[f_lost_person] == 0 and remains[remains_person] > 1:
                remains[f_lost_person] += 1
                remains[remains_person] -= 1
                
        if e_lost_person <= n-1:
            if remains[e_lost_person] == 0 and remains[remains_person] > 1:
                remains[e_lost_person] += 1
                remains[remains_person] -= 1
    # count    
    for i in remains:
        if i >= 1:
            answer += 1
        
    return answer


print(solution(n,lost, reserve))