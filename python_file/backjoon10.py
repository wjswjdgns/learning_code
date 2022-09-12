from collections import deque
def solution(word, depth, idx, L, C):

    if depth == L:
        result_list.append(word)
        return

    for i in range(idx, C): #움직이는 인덱스부터 value_list의 끝까지 진행
        solution(word+value_list[i], depth+1, i+1, L, C)
        
L,C = map(int, input().split()) # L개의 알파벳 C만큼의 
value_list = input().split() #
value_list.sort()

# 변수 설정
depth = 0 #총 길이
idx = 0 # 움직이는 인덱스
result_list = deque()
word = ''
check_list = ['a', 'e', 'i', 'o', 'u'] #체크 리스트

solution(word ,depth, idx, L,C)

#패스워드 확인
for password in result_list:
    collection = 0 #모음확인
    consonant = 0 #자음확인
    
    for p_word in password:
        if p_word in check_list:
            collection+=1
        else:
            consonant+=1
    
    if collection >= 1 and consonant >= 2:
        print(password)
