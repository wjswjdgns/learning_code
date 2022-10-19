"""
와인 동일 잔 따르기
#1
N = int(input())
value_list = list(map(int, input().split()))
count = 1
while True:
	value_list.sort()
	for i in range(N-1):
		value_list[i] += 1
	
	if sum(value_list) == value_list[0]*N:
		break
	
	count +=1

print(count)
"""

"""
중복 빼고 나머지

n = int(input())
value_list = list(map(int, input().split()))
value_list.sort()
stack = []

for i in value_list:
	if stack == False:
		stack.append(i)
	else:
		if i in stack:
			stack.pop()
		else:
			stack.append(i)

print(stack[0])

"""

"""
n,m,k = map(int, input().split()) # n : 귀족, m : 상인, k : 시민
n_value = list(map(int, input().split())) #2
m_value = list(map(int, input().split())) #3
k_value = list(map(int, input().split())) #1

value_list = n_value + m_value + k_value
set_value_list = list(set(n_value + m_value + k_value)) # 중복 없앰
set_value_list.sort()
dic = {i:0 for i in set_value_list}

for idx,value in enumerate(value_list):
	if idx+1 <= n:
		count = 2
	elif idx+1 <= n+m:
		count = 3
	else: 
		count = 1
		
	dic[value] += count
	
print(max(dic, key = dic.get))

"""

def cal(r_hour, r_min, hour, minute):
    if r_hour == hour and r_min == minute:
        return (0,0)
    result = []
    return_hour = 0
    return_min = 0
    if 21 <= r_hour < 24: # b계산법 적용
        hour += 24
        if r_min > minute:
            r_min += 60
        return_hour = hour - r_hour
        return_min = minute - r_min
        result.append((return_hour,return_min)) 
    else: #a계산법 적용
        return_hour = max(r_hour,hour) - min(r_hour,hour)
        return_min = max(r_min, minute) - min(r_min,minute)
        result.append((return_hour, return_min))
        
    return result

n, k = map(int, input().split())
value_list = []
for _ in range(n):
	 value_list.append(list(input().split()))

dic = {i[1]:[] for i in value_list}
visited = []
check = []

for time, name in value_list:
    time_list = time.partition(':')
    hour = int(time_list[0])
    minute = int(time_list[2])
    
    #이미 출입을 했다면 공부 시간 계산
    if name in visited:
        index = visited.index(name)
        visited.remove(name)
        
        r_hour = check[index][0] #출입 시간
        r_min = check[index][1] # 출입 분
        
        dic[name].append(cal(r_hour,r_min,hour,minute))
        del check[index]
        
    # 출입 했을 때 기록만
    else:
        visited.append(name)
        check.append([hour,minute])

#합격자 발표
goal = 0
for i in dic.values():
    h = 0
    m = 0
    for j in i:
        h += j[0][0]
        m += j[0][1]
    
    if m >= 60: # 합한 분이 60을 넘었을 때 1시간 추가
        h += 1

    if h >= k:
        goal +=1

print(goal)
    
        
        


    
