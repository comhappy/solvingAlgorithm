# 색종이 붙이기

def checkpaper(x, y, r):    # 색종이 사용가능 여부 확인
    if 0 <= x + r < 10 and 0 <= y + r < 10:
        for i in range(r + 1):
            for j in range(r + 1):
                if graph[x + i][y + j] == 0:
                    return False
    else:
        return False

    return True


def fillpaper(x, y, r, l): # 색종이 채우기, 비우기
    global remain

    for i in range(r + 1):
        for j in range(r + 1):
            graph[x + i][y + j] = l

    if l == 1:
        remain += (r + 1) * (r + 1)
    elif l == 0:
        remain -= (r + 1) * (r + 1)


def DFS(i):  # 색종이의 왼쪽 위 좌표
    global answer

    if sum(paper) >= answer:
        return

    x = i // 10
    y = i % 10

    for r in range(4, -1, -1):  # 추가되는 색종이 변의 길이
        if paper[r] >= 5:   # 색종이 사용개수가 5개 이상인 경우, 사용불가
            continue

        if checkpaper(x, y, r): # 색종이 사용 가능
            fillpaper(x, y, r, 0)
            paper[r] += 1

            if remain == 0:   # 정답인 경우
                answer = min(answer, sum(paper))

                # 원상복구
                fillpaper(x, y, r, 1)
                paper[r] -= 1

                return
            else:
                for k in range(i + r + 1, 100):
                    nx = k // 10
                    ny = k % 10

                    if graph[nx][ny] == 1:
                        DFS(k)
                        break

                # 원상복구
                fillpaper(x, y, r, 1)
                paper[r] -= 1


graph = list(list(map(int, input().split())) for _ in range(10))
paper = [0 for _ in range(5)]   # 사용한 색종이 개수
answer = 26

remain = sum(sum(i) for i in graph)

if remain == 0:
    print(0)
else:
    for i in range(100):
        x = i // 10
        y = i % 10

        if graph[x][y] == 1:
            DFS(i)
            break

    if answer == 26:
        print(-1)
    else:
        print(answer)