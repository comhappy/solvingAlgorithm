import sys
sys.setrecursionlimit(10**6)

# BackTracking 문제

def DFS(num, p):
    if len(p) == M:     # 출력해야하는 경우
        for i in p:
            print(i, end=' ')
        print()

        return False
    else:       # 원소를 추가해야하는 경우
        for i in range(num + 1, N + 1):
            p.append(i)
            DFS(i, p)
            p.pop()

        return True


N, M = map(int, input().split())

for i in range(1, N + 1):
    DFS(i, [i])