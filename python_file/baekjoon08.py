#팩토리얼 구하는 식
#자릿수 확인 하는 것
#dic (n-idx)

import sys
fectorial_dic = {1:1, 2:2, 3:6, 4:24, 5:120}
while True:
    value_list = list(map(int, sys.stdin.readline().rstrip()))
    if value_list[0] == 0:
        break
    
    N = len(value_list)
    result = 0
    
    for i in range(N): #0, 1 ,2
        value = value_list[i] # i
        idx = N-i
        result = result + (value * fectorial_dic[idx])

    if result != 0:
        print(result) 

