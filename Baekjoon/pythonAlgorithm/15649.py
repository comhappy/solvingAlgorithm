# N과 M, 1~N까지의 수 중, 중복없이 M개를 고른 수열을 출력

def DFS(e, p):
    p.append(e)
    
    if len(p) == M: # 출력하는 경우
        for i in p:
            print(i, end=' ')
        print()
        p.pop() # 해당 상태로 돌아가기 위한 pop

        return False
    else:   # 숫자를 추가하는 경우
        for i in range(1, N + 1):
            if i not in p:  # 같은 숫자는 들어갈 수 없음.
                DFS(i, p)
        p.pop()

        return True

N, M = map(int, input().split())

for i in range(1, N + 1):
    p = list()
    DFS(i, p)