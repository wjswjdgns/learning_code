n = 5
arr1 = [9,20,28,18,11]
arr2 = [30,1,21,17,28]

def cal(num1,num2):
    result = ''
    value01 = []
    value02 = []
    for i in range(5): #2진수 확인
        value01.insert(0,str(num1%2))
        num1 = num1//2

        value02.insert(0,str(num2%2))
        num2 = num2//2
    
    for i in range(5): #  #둘다 공백인 경우 공백 나머지는 벽
        if value01[i] == '0' and value02[i] =='0':
            result += ' '
        else:
            result += '#'  
    return result

def solution(n, arr1, arr2):
    answer = []
    for arr1_num,arr2_num in zip(arr1,arr2):
        answer.append(cal(arr1_num,arr2_num))
    return answer

print(solution(n,arr1,arr2))


