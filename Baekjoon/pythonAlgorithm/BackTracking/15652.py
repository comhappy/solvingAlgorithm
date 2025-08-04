# N과 M 문제

def DFS(num, p):
    if len(p) == M: # 정답을 출력하는 경우
        for i in p:
            print(i, end=' ')
        print()
    else:   # 원소를 추가하는 경우
        for i in range(num, N + 1):
            p.append(i)
            DFS(i, p)
            p.pop()

        return True


N, M = map(int, input().split())

for i in range(1, N + 1):
    DFS(i, [i])