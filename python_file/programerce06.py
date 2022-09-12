def solution(participant, completion):
    hash_dic = {}
    sum_value = 0
    
    for p in participant:
        dic_num = hash(p)
        hash_dic[dic_num] = p
        sum_value+=dic_num
        
    for p in completion:
        sum_value -= hash(p)
    
    answer = hash_dic[sum_value]
    return answer

#주어진 값을 해싱작업

#주어진 해싱 값을 푸는 작업 필요

