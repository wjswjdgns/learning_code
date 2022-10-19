# 탐욕법 거스름돈

N = int(input())

return_value = 1000 - N
count = 0
while return_value:

    #500원
    if return_value >=500:
        count+= return_value//500
        return_value = return_value - (500 *(return_value//500))
    elif return_value >= 100:
        count += return_value//100
        return_value = return_value - (100*(return_value//100))
    elif return_value >= 50:
        count+= return_value//50
        return_value =return_value - (50*(return_value//50))
    elif return_value >= 10:
        count+= return_value //10
        return_value = return_value - (10*(return_value//10))
    elif return_value >= 5:
        count+=return_value//5
        return_value = return_value - (5*(return_value//5))
    else:
        count+=return_value
        tmp = return_value
        return_value = return_value - tmp
        
    
print(count)        
