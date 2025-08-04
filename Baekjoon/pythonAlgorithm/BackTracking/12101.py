# 1, 2, 3 더하기 2

def DFS(number, sum):
    global index

    if index == k:
        return

    if sum == n:    # 정답을 구한 경우
        index += 1

        if index == k:
            print(*number, sep="+")
        return
    elif sum > n:
        return
    else:
        for i in range(1, 4):
            number.append(i)
            DFS(number, sum + i)
            number.pop()


n, k = map(int, input().split())

index = 0
DFS([], 0)

if index != k:
    print(-1)