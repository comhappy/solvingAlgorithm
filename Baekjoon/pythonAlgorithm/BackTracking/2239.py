# 스도쿠
def DFS(index):
    global answer

    x = index // 9
    y = index % 9

    for i in range(9):
        if index in square[i]:
            square_index = i
            break

    if answer == 1:
        return
    elif index == 81: # 끝나는 경우
        for i in sdoku:
            print(*i, sep='')
        
        answer = 1

        return
    elif sdoku[x][y] == 0:    # 숫자를 채워야하는 경우
        for i in range(1, 10):
            # 값을 넣을 수 있는지 확인
            if visited_x[x][i] == 0 and visited_y[y][i] == 0 and visited_square[square_index][i] == 0:
                visited_x[x][i] = 1
                visited_y[y][i] = 1
                visited_square[square_index][i] = 1
                sdoku[x][y] = i

                DFS(index + 1)

                visited_x[x][i] = 0
                visited_y[y][i] = 0
                visited_square[square_index][i] = 0
                sdoku[x][y] = 0
    else:   # 이미 숫자가 있는 경우
        DFS(index + 1)


sdoku = list(list(int(i) for i in input()) for _ in range(9))

# 작은 정사각형을 이루는 index
square = [[0, 1, 2, 9, 10, 11, 18, 19, 20],
          [3, 4, 5, 12, 13, 14, 21, 22, 23],
          [6, 7, 8, 15, 16, 17, 24, 25, 26],
          [27, 28, 29, 36, 37, 38, 45, 46, 47],
          [30, 31, 32, 39, 40, 41, 48, 49, 50],
          [33, 34, 35,  42, 43, 44, 51, 52, 53],
          [54, 55, 56, 63, 64, 65, 72, 73, 74],
          [57, 58, 59, 66, 67, 68, 75, 76, 77],
          [60, 61, 62, 69, 70, 71, 78, 79, 80]]

visited_x = [[0 for _ in range(10)] for _ in range(9)]
visited_y = [[0 for _ in range(10)] for _ in range(9)]
visited_square = [[0 for _ in range(10)] for _ in range(9)]

# 방문처리
for index in range(81):
    x = index // 9
    y = index % 9

    visited_x[x][sdoku[x][y]] = 1
    visited_y[y][sdoku[x][y]] = 1

    for j in range(9):
        if index in square[j]:
            square_index = j
            break

    visited_square[square_index][sdoku[x][y]] = 1

answer = 0
DFS(0)