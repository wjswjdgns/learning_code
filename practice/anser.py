import sys
input = sys.stdin.readline

n, k = map(int, input().split())
matrix = dict()
chk = k * 60
for i in range(n):
    t, n = map(str, input().split())
    if n not in matrix:
        matrix[n] = [ 1 , t, 0]
    else:
        if matrix[n][0] == 1:
            st = matrix[n][1].split(':')
            ed = t.split(":")

            ger_ed = int(ed[0])*60 + int(ed[1])
            ger_st = int(st[0])*60 + int(st[1])
            matrix[n][0] = 2
            if ger_ed < ger_st:

                matrix[n][2] += (1440 - ger_st) + ger_ed
            else:
                matrix[n][2] += ger_ed - ger_st
        elif matrix[n][0] == 2:
            matrix[n][1] = t
            matrix[n][0] = 1
res = 0
for i in matrix:
    if matrix[i][2] >= chk:
        res += 1
print(res)