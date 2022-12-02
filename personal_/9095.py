# 1,2,3 더하기
# dp

T = int(input())

def cal(data):
    idx = data -1
    if data == 1:
        return 1
    elif data == 2:
        return 2
    elif data == 3:
        return 4
    
    if memo[idx] == 0:
        memo[idx] = cal(data-1) + cal(data-2) + cal(data-3)

    return memo[idx]

for testcase in range(T):
    N = int(input())
    memo = [0 for _ in range(N)] # n의 갯수 만큼 전부 만든다
    print(cal(N))
    

    # 1을 만드는 방법

    # 2를 만드는 방법

    # 3을 만드는 방법


