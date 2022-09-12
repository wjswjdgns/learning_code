# 입력값 설정

L = int(input()) # 문자 길이
word = input() #주어진 문자

#변수 설정
check_dic = {i:idx+1 for idx, i in enumerate('abcdefghijklmnopqrstuvwxyz')}
r = 31
M = 1234567891

result = 0
for idx,w in enumerate(word):
    word_number = check_dic[w]
    result += word_number * (r**idx)

print(result%M)