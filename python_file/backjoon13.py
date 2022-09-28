# 백준 1463번 1로 만들기

"""
조건
1. 3으로 나누어 떨어뜨려지면 3으로 나눈다
2. 2로 나누어 떨어뜨려지면 2로 나눈다.
3. 1을 뺀다.

1을 먼저 빼본 결과가 3의 공배수 일 경우 1을 빼는 것을 먼저 실행
기본적으로 최소횟수를 만들기 위해서는 2보다는 3으로 먼저 나눌 수 있도록 해야 한다.

메모이제이션
"""

"""
# 2차 코드
def solution(N):
    global result
    count = 1
    result.append([])

    if N%3 == 0:
        result[0].append(N//3)
    if N%2 == 0:
        result[0].append(N//2)
    if N-1 != 0:
        result[0].append(N-1)

    while True:
        if 1 in result[count-1]:
            break
        result.append([])
        for value in result[count-1]:
            if value%3 == 0:
                result[count].append(value//3)
            if value%2 == 0:
                result[count].append(value//2)
            if value-1 != 0:
                result[count].append(value-1)
        count+=1
    return count

N = int(input())
result = []
print(solution(N))

"""

"""
# 3차 코드
def solution(count,value):

    if value == 1: # 1에 도달 했을 경우 return
        count_list.append(count)
        return
    if value in dic: #동일한 계산 방법이 있을 경우 생략
        if 1 in dic[value]:
            count+=1
            count_list.append(count)
        return

    # N에 대한 모든 경우를 dic에 추가
    dic[value] = []
    if value%3 == 0:
        dic[value].append(value//3)
        solution(count+1,value//3)
    if value%2 == 0:
        dic[value].append(value//2)
        solution(count+1,value//2)
    if value-1 != 0:
        dic[value].append(value-1)
        solution(count+1, value-1)
        
N = int(input())
dic = {}
count_list = []
solution(0,N)
print(min(count_list))
"""


# 4차 코드
# 낮은 숫자부터 주어진 규칙을 적용하여 나올 수 있는 경우의 수를 확인
# 해당 경우의 수중 최솟값을 memo에 적용

N = int(input())
memo = [0] * (N+1) # N의 까지의 결과를 메모 진행할 리스트

for i in range(2, N+1): #작은 숫자 0과 1은 해당 규칙을 적용할 수 없기에 제외
    memo[i] = memo[i-1] + 1 #이전 결과에 한번의 count 추가 (2와 3을 나눌 수 없는 경우)

    # 2로 나누어 질 경우 (단순히 빼었을 때와 2와 나누었을때 두가지 케이스를 가지 수 확인) --> 최솟값 적용
    if i%2 == 0:
        memo[i] = min(memo[i], memo[i//2]+1) 

    # 3로 나누어 질 경우 (단순히 빼었을 때와 3와 나누었을때 두가지 케이스를 가지 수 확인) --> 최솟값 적용
    if i%3 == 0:
        memo[i] = min(memo[i], memo[i//3]+1) 
    
print(memo[N])

