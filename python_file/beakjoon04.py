### 분류 작업 함수

def soultion(arr,idx):
    if len(arr) == 0:
        result.append(0)
        return

    global check_card
    pivot = len(arr)//2 # 중앙 기준 값

    if arr[pivot] == check_card[idx]: #user_card의 중앙값과 check_card의 값과 동일 했을 때
        result.append(arr.count(arr[pivot])) #user_card에서 해당 값의 전체 갯수를 result에 추가
        return
    elif arr[pivot] > check_card[idx]:
        soultion(arr[:pivot], idx)
    elif arr[pivot] < check_card[idx]:
        soultion(arr[pivot+1:], idx)



### 입력 값 ---------
"""
N = int(input())
user_card = list(map(int, input().split())) #상근이가 들고 있는 카드

M = int(input())
check_card = list(map(int,input().split())) #확인해야 하는 카드
"""

##임시 테스트 변수
N = 10
M = 8
user_card = [6,3,2,10,10,10,-10,-10,7,3]
check_card = [10,9,-5,2,3,4,5,-10]

### 필요 변수 ---------
end = len(check_card)
result = [] #결과값 리스트
user_card.sort() #정렬

print(user_card)

### 체크
for i in range(end):
    soultion(user_card,i)
        
### 결과 노출
print(result)


