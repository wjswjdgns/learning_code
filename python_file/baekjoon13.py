def solution(base):
    if base <= 1:
        result_list.insert(0, str(base))
        return
    result_list.insert(0, str(base%2))
    solution(base//2)
    return

N = int(input())
result_list = []
solution(N)

if result_list[0] == '0':
    result_list = result_list[1:]
    print(int(''.join(result_list)))

else:
    print(int(''.join(result_list)))
