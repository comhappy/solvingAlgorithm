# 숫자 재배치

def DFS(num):
    global answer

    if len(num) == len(a):  # 숫자가 만들어진 경우
        if int(num) < int(b):
            answer = max(answer, int(num))
    elif num[0] == "0":
        return
    else:
        for i in range(len(a)):
            if visited[i] == 0:
                visited[i] = 1
                DFS(num + a[i])
                visited[i] = 0


a, b = map(str, input().split())
visited = [0 for _ in range(len(a))]
answer = -1

for i in range(len(a)):
    visited[i] = 1
    DFS(a[i])
    visited[i] = 0

print(answer)