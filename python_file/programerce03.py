n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

def solution(n, results):
    win_game = [[] for _ in range(n)]
    lose_game = [[] for _ in range(n)]
    
    answer = 0
    for w,l in results:
        win_game[w-1].append(l) #자신이 이긴 사람을 등록
        lose_game[l-1].append(w) #자신을 이긴 사람을 등록
    
    for i in range(n): #1부터 n까지 진행
        for win in win_game[i]: # win = i가 이긴 사람 i > win
            # lose_game[i] = i를 이긴 사람 lose_game[win] = win을 이긴 사람
            lose_game[win-1] = list(set(lose_game[win-1] + lose_game[i])) #win를 이긴 사람 목록에 i를 이긴 사람 목록 추가
        for lose in lose_game[i]: # lose = i를 이긴 사람 i < lose
            win_game[lose-1] = list(set(win_game[lose-1] + win_game[i])) #lose가 이긴 사람 목록에  i가 이긴 사람 목록 추가
    
    for i in range(n):
        if len(lose_game[i]) + len(win_game[i]) == n-1:
            answer += 1

    return answer

print(solution(n, results))