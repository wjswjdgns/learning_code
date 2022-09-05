T = int(input())
value_list = [None] * T 

def stack(value):
    if value[0] == ')':
        return 'NO'

    value_len = len(value)
    return_list = [None]*value_len
    count = 0
    for stack_value in value:
        if stack_value == '(':
            return_list[count] = stack_value
            count += 1
        else:
            # ) 만 남아 있는 경우를 생각하라
            if '(' not in return_list:
                return 'NO'
            else:
                count -= 1
                return_list[count] = None
    
    if '(' in return_list:
        return 'NO'
    else:
        return 'YES'
        

#반복 입력 확인
for i in range(T):
    value_list[i] = input()

for j in value_list:
    print(stack(j))



#스택 하나 만들고 '(' 가 나온 갯수 만큼 ')' 가 나와야 한다. 갯수가 틀릴 경우 False 처리
