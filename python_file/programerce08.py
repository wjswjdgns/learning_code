# 올바른 괄호, 균형잡힌 괄호 확인 

"""
1. 
2. 
3. 
  
4. 
  4-1.  /* answer += '(' */
  4-2. 
  4-3. 
  4-4. 
  4-5. 
"""


from collections import deque
#p = '(()())()' 
#p = ')('
p = '()))((()'

# u(균형 잡힌 괄호) 와 v로 분리

def divide(p):
    #p의 괄호 카운트 변수
    u_count = 0 # '('
    v_count = 0 # ')'

    # 스캔을 진행하면서 u와 v를 분리 (v_count, u_count 두개가 같아 지는 순간)
    for idx in range(len(p)):
        if p[idx] == '(':
            u_count+=1
        else:
            v_count+=1
        
        if u_count == v_count:
            return p[:idx+1], p[idx+1:]
           
def check(u):
    # u가 '올바른 괄호 문자열'인지 확인
    check_stack = deque()
    for u_value in u:
        if u_value == '(':
            check_stack.append(u_value)
        else:
            if '(' in check_stack:
                check_stack.pop()
            else:
                return False
    return True

def solution(p):
    # 1단계 : 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
    if p == '':
        return ''

    # 2단계 : 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
    u, v = divide(p) # u와 v값으로 나누기

    # 3단계 : 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
    # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 

    if check(u): # u 값이 '올바른 괄호 문자열' 일 경우
        return u + solution(v) #u를 붙이고 1단계부터 시작 3

    # 4단계 : 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
    else:
        answer = '(' # 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
        answer += solution(v) #문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
        answer += ')'         #')'를 다시 붙입니다. 
        
        
        #u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
        for u_value in u[1:len(u)-1]:
            if u_value == '(':
                answer += ')'
            else:
                answer += '('
                
    return answer #생성된 문자열을 반환합니다.

print(solution(p))