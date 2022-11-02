
operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
#operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]	

import heapq
def solution(operations):
    # [최댓값, 최솟값]
    answer = []
    heap = []
    for command in operations:
        if command[0] == 'I': #삽입
            heapq.heappush(heap,int(command[2:]))
        else:
            if bool(heap) == False:
                continue
            if int(command[2:]) == -1: # 최솟값
                heapq.heappop(heap)
            else: # 최댓갑
                heap.remove(heapq.nlargest(1, heap)[0])
    if bool(heap) == False:
        answer = [0,0]
    else:
        min = heapq.nsmallest(1, heap)[0]
        max = heapq.nlargest(1, heap)[0]
        answer = [max, min]
        pass
    return answer

print(solution(operations))