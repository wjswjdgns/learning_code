N = int(input())

tree = [[] for _ in range(N)] # 자식 + 부모를 담은  리스트 생성 (부모를 걸러내는 작업 필요)
parents = [0 for _ in range(N)] # 부모를 기억하는 리스트

for i in range(N-1):
    value01, value02 = map(int, input().split())
    
    # 주어진 value01과 value02 중 어떤 것이 부모인지 알 수 없기 때문에 전부 넣고 추후 분류 진행
    tree[value01-1].append(value02)
    tree[value02-1].append(value01)

def search_parents(target, target_values):
    #tree에 담겨진 정보를 바탕으로 서칭 진행
    for z in target_values:
        if parents[z-1] == 0: # 해당 번호의 등록된 부모 값이 없을 경우
            parents[z-1] = target #부모값 등록
            search_parents(z, tree[z-1]) #해방 번호의 자식 + 부모 값으로 넘어가서 재확인
        
        #이미 부모 값이 있다면 더 이상 부모를 등록하지 않고 넘어가게 된다 (tree에서 섞여 있는 데이터 걸러내기)

#부모를 확인하는 함수 진행 (루트는 1이라고 했기 때문에 1로 진행)
search_parents(1, tree[0])

print(parents)