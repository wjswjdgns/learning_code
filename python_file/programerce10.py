# 힙, 더 맵게

import heapq

scoville = [1,2,3,9,10,12]
K = 7


def solution(scoville, k):
    answer = 0
    heapq.heapify(scoville) # 주어진 리스트를 힙 구조로 변경
    
    while scoville[0] < k and len(scoville) != 1:
        min_one = heapq.heappop(scoville)
        min_two = heapq.heappop(scoville)

        # 계산진행
        new_scov = min_one + (min_two * 2)
        heapq.heappush(scoville, new_scov) #추가

        answer +=1
    
    if scoville[0] < k:
        return -1
    else:
        return answer

solution(scoville,K)