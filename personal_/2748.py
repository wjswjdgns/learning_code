# dp 문제
# 피보나치2 

n = int(input())
memo = [0 for _ in range(n)] # 메모리제이션


def pibo(num):
    idx = num - 1
    if num == 1 or num == 2:
        return 1

    if memo[idx] == 0:
        memo[idx] = pibo(num-1) + pibo(num-2)

    return memo[idx]
        

print(pibo(n))