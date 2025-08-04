# 계란으로 계란치기

import sys
input = sys.stdin.readline

def DFS(egg):
    global answer

    if egg == n:
        answer = max(answer, sum(visited))
        return
    elif visited[egg] == 1:
        DFS(egg + 1)
        return
    else:
        broken = False
        for i in range(n):
            if visited[i] == 0 and i != egg:    # 깨려는 계란이 깨져있지 않고 손에 든 계란이 아닌 경우
                broken = True
                s[egg] -= w[i]
                s[i] -= w[egg]

                if s[egg] <= 0 and s[i] <= 0:   # 둘다 깨진 경우우
                    visited[egg] = 1
                    visited[i] = 1
                    DFS(egg + 1)
                    visited[egg] = 0
                    visited[i] = 0

                elif s[egg] <= 0 and s[i] > 0:  # 손에 든 계란만 깨진 경우
                    visited[egg] = 1
                    DFS(egg + 1)
                    visited[egg] = 0

                elif s[egg] > 0 and s[i] <= 0: # 치는 계란만 깨진 경우
                    visited[i] = 1
                    DFS(egg + 1)
                    visited[i] = 0

                elif s[egg] > 0 and s[i] > 0: # 안깨진 경우
                    DFS(egg + 1)

                s[egg] += w[i]
                s[i] += w[egg]

        if broken == False:
            DFS(egg + 1)


n = int(input())
s = list()
w = list()

for _ in range(n):
    si, wi = map(int, input().split())

    s.append(si)
    w.append(wi)
    
answer = 0
visited = [0 for _ in range(n)] # 계란이 깨진 경우 1
DFS(0)
print(answer)