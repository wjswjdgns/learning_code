import time
start = time.time()

from collections import deque

N = int(input())
de_q = deque([i for i in range(1, N+1)])

while len(de_q) > 1:
    de_q.popleft()
    value = de_q.popleft()
    de_q.append(value)

print(de_q[0])
print("time : ", time.time() - start)

## 해당 백준 문제에서는 처음부터 나누는 방식은 정답처리로 진행하지 않는다. 


start = time.time() 

N = int(input())
de_q = deque(i for i in range(1,N+1))

"""
# 처음 루틴을 돌게 되면 홀수는 빠지고 짝수만 남게 된다.=
1,2,3,4,5,6
2,3,4,5,6 #1제외
3,4,5,6,2 #2뒤로
4,5,6,2 #3제외
5,6,2,4 #4뒤로
6,2,4 #5제외
2,4,6 #6뒤로

1,2,3,4,5,6,7
2,3,4,5,6,7 #1제외
3,4,5,6,7,2 #2뒤로
4,5,6,7,2 #3제외
5,6,7,2,4 #4뒤로
6,7,2,4 #5제외
7,2,4,6 #6뒤로
2,4,6 #7제외

1,2,3,4,5,6,7,8
2,3,4,5,6,7,8 #1제외
3,4,5,6,7,8,2 #2뒤로
4,5,6,7,8,2 #3제외
5,6,7,8,2,4 #4뒤로
6,7,8,2,4 #5제외
7,8,2,4,6 #6뒤로
8,2,4,6 # 7제외
2,4,6,8 # 8뒤로
"""