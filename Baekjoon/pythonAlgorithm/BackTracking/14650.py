# 걷다보니 신천역 삼(small)

def DFS(num, depth):
    global answer

    if n == depth:
        if len(str(num)) == n:
            if num != 0 and num % 3 == 0:
                answer += 1
            return
    else:
        for i in range(3):
            DFS(num * 10 + i, depth + 1)


n = int(input())

answer = 0
DFS(0, 0)
print(answer)