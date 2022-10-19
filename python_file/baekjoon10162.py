# A : 5분 B : 10분 C : 10초

T = int(input())

count = []
result = T
check = True

while result:
    count.append(result//300)
    result = result - (300 * (result//300))
    
    count.append(result//60)
    result = result - (60 * (result//60))
    
    count.append(result//10)
    result = result - (10 * (result//10))
    
    if result != 0:
        check = False
        break

if check == False:
    print(-1)
else:
    for i in count:
        print(i, end=" ")