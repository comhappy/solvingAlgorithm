# 크면서 작은 수

def DFS(depth, num):
    global answer

    if depth == len(x):
        if num_x < num < answer:
            answer = num
        return
    else:
        for i in range(len(x)):
            if visited[i] == 0:
                visited[i] = 1
                DFS(depth + 1, 10 * num + int(x[i]))
                visited[i] = 0


x = input()
num_x = int("".join(i for i in x))
visited = [0 for _ in range(len(x))]
answer = 999999

DFS(0, 0)

if answer == 999999:
    print(0)
else:
    print(answer)