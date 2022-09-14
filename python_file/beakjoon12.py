"""
# 1번
def solution(depth):
    if depth == M:
        print(' '.join(map(str, result)))
        return

    for i in range(0, N):
        if value_list[i] not in result:
            result.append(value_list[i])
            solution(depth+1)
            result.pop()

N,M = map(int, input().split())
value_list = [i for i in range(1,N+1)]
result = []
solution(0) #깊이, 현재 위치, 최대 길이, 나와야 하는 길이
"""

"""
# 2번
def solution(depth, idx):
    if depth == M:
        print(' '.join(map(str, result)))
        return

    for i in range(idx, N):
        result.append(value_list[i])
        solution(depth+1, i+1)
        result.pop()

N,M = map(int, input().split())
value_list = [i for i in range(1,N+1)]
result = []
solution(0,0) #깊이, 현재 위치, 최대 길이, 나와야 하는 길이
"""

"""
# 3번
def solution(depth):
    if depth == M:
        print(' '.join(map(str, result)))
        return

    for i in range(0, N):
        result.append(value_list[i])
        solution(depth+1)
        result.pop()

N,M = map(int, input().split())
value_list = [i for i in range(1,N+1)]
result = []
solution(0) #깊이, 현재 위치, 최대 길이, 나와야 하는 길이
"""

"""
#4번
def solution(depth, idx):
    if depth == M:
        print(' '.join(map(str, result)))
        return

    for i in range(idx, N):
        result.append(value_list[i])
        solution(depth+1, i)
        result.pop()

N,M = map(int, input().split())
value_list = [i for i in range(1,N+1)]
result = []
solution(0,0) #깊이, 현재 위치, 최대 길이, 나와야 하는 길이
"""

"""
#5번
def solution(depth):
    if depth == M:
        print(' '.join(map(str, result)))
        return

    for i in range(0, N):
        if value_list[i] not in result:
            result.append(value_list[i])
            solution(depth+1)
            result.pop()

N,M = map(int, input().split())
value_list = list(map(int, input().split()))
value_list.sort()
result = []
solution(0) #깊이, 현재 위치, 최대 길이, 나와야 하는 길이

"""

"""
#6번
def solution(depth,idx):
    if depth == M:
        print(' '.join(map(str, result)))
        return

    for i in range(idx, N):
        result.append(value_list[i])
        solution(depth+1,i+1)
        result.pop()

N,M = map(int, input().split())
value_list = list(map(int, input().split()))
value_list.sort()
result = []
solution(0,0) #깊이, 현재 위치, 최대 길이, 나와야 하는 길이

"""

"""
#7번
def solution(depth):
    if depth == M:
        print(' '.join(map(str, result)))
        return

    for i in range(0, N):
        result.append(value_list[i])
        solution(depth+1)
        result.pop()

N,M = map(int, input().split())
value_list = list(map(int, input().split()))
value_list.sort()
result = []
solution(0) #깊이, 현재 위치, 최대 길이, 나와야 하는 길이
"""

"""
# 8번
def solution(depth,idx):
    if depth == M:
        print(' '.join(map(str, result)))
        return

    for i in range(idx, N):
        result.append(value_list[i])
        solution(depth+1, i)
        result.pop()

N,M = map(int, input().split())
value_list = list(map(int, input().split()))
value_list.sort()
result = []
solution(0,0) #깊이, 현재 위치, 최대 길이, 나와야 하는 길이
"""

"""
#9번 -->  중복값
def solution(depth):
    if depth == M:
        print(' '.join(map(str, result)))
        return
    tmp = 0
    for i in range(0, N):
        if visited[i] != 1 and tmp != value_list[i]:
            result.append(value_list[i])
            tmp = value_list[i] #visited를 통해서 앞에 9는 넘어가기 때문에 tmp는 7로 유지상태로 다음 9로 넘어감
            visited[i] = 1
            solution(depth+1)
            result.pop()
            visited[i] = 0

N,M = map(int, input().split())
value_list = list(map(int, input().split()))

visited = [0 for _ in range(N)]
value_list.sort()
result = []

solution(0) #깊이, 현재 위치, 최대 길이, 나와야 하는 길이

"""

"""
#10번
def solution(depth,idx):
    if depth == M:
        print(' '.join(map(str, result)))
        return
    tmp = 0
    for i in range(idx, N):
        if visited[i] != 1 and tmp != value_list[i]:
            result.append(value_list[i])
            tmp = value_list[i] #visited를 통해서 앞에 9는 넘어가기 때문에 tmp는 7로 유지상태로 다음 9로 넘어감
            visited[i] = 1
            solution(depth+1, i+1)
            result.pop()
            visited[i] = 0

N,M = map(int, input().split())
value_list = list(map(int, input().split()))

visited = [0 for _ in range(N)]
value_list.sort()
result = []

solution(0,0) #깊이, 현재 위치, 최대 길이, 나와야 하는 길이
"""

"""
# 11번
def solution(depth):
    if depth == M:
        print(' '.join(map(str, result)))
        return
    tmp = 0
    for i in range(0, N):
        if tmp != value_list[i]:
            result.append(value_list[i])
            tmp = value_list[i] #visited를 통해서 앞에 9는 넘어가기 때문에 tmp는 7로 유지상태로 다음 9로 넘어감
            solution(depth+1)
            result.pop()
            

N,M = map(int, input().split())
value_list = list(map(int, input().split()))

value_list.sort()
result = []

solution(0) #깊이, 현재 위치, 최대 길이, 나와야 하는 길이

"""

def solution(depth,idx):
    if depth == M:
        print(' '.join(map(str, result)))
        return
    tmp = 0
    for i in range(idx, N):
        if tmp != value_list[i]:
            result.append(value_list[i])
            tmp = value_list[i] #visited를 통해서 앞에 9는 넘어가기 때문에 tmp는 7로 유지상태로 다음 9로 넘어감
            solution(depth+1, i)
            result.pop()
            

N,M = map(int, input().split())
value_list = list(map(int, input().split()))

value_list.sort()
result = []

solution(0,0) #깊이, 현재 위치, 최대 길이, 나와야 하는 길이