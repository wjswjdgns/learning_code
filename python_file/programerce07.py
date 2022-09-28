def solution(phone_book):
    answer = True
    phone_book.sort()
    
    for idx,i in enumerate(phone_book):
        base = i
        length = len(base)
        
        for i in phone_book[idx+1:]:
            if i[:length] == base:
                answer = False
                break
        if answer == False:
            break   
    return answer

#### 

def solution(phone_book):
    answer = True
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len((phone_book[i]))]:
            answer = False
            break
    return answer


# 재귀함수 괄호변환
# 부분집합 일곱난쟁이
# 동적계획법 1로 만들기
# 동적계획법 가장 긴 증가하는 부분 수열


