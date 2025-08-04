# 좋은수열

def DFS(depth, num):
    global answer

    if answer == 0:     # 정답이 구해지지 않은 경우

        # 좋은수열 검사
        k = 1
        for j in range(depth - 2, -1, -2):  # 역순으로 2개씩
            if num[j:j+k] == num[j+k:]:
                return
            k += 1

        if depth == n:  # 길이가 도달한 경우
            answer = int(num)
            return
        else:
            for i in range(1, 4):
                DFS(depth + 1, num + str(i))


n = int(input())
answer = 0

DFS(1, "1")
DFS(1, "2")
DFS(1, "3")

print(answer)