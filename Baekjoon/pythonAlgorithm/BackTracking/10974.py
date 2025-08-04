# 모든 순열

def DFS():
    if len(answer) == N:
        print(" ".join(map(str, answer)))

        return
    else:
        for i in range(1, N + 1):
            if i not in answer:
                answer.append(i)
                DFS()
                answer.pop()

        return

N = int(input())
answer = list()

DFS()