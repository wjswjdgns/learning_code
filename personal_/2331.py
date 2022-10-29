# 1. 4자리까지 분리해서 확인
# 2. 각 자리수를 구한 값을 더한 값을 다음 숫자로 확인
# 3. 반복되는 구간부터 삭제
# 4. 남은 값들을 출력

import sys
input = sys.stdin.readline
A,P = map(int, input().split())
check = [A]
while True:
    start_num = check[-1]
    new_value = 0
    for num in str(start_num):
        new_value = new_value + (int(num)**P) #다음 값 확인

    if new_value not in check:
        check.append(new_value)
    else:
        f_index = check.index(new_value)
        result =  check[:f_index]
        break

print(len(result))
    