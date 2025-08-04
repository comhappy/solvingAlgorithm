# 주사위 윷놀이

def move_cal_x(point, dice):    # 말의 이동과 점수계산을 해주는 함수    
    cur_point = point

    for _ in range(dice):
        next_point = graph[cur_point][0]    # 말 이동
        cur_point = next_point

        if cur_point == 32: # 말이 도착한 경우
            break

    return cur_point, score[cur_point]


def DFS(num):
    global answer, x_point, x_score

    if num == 10:   # 주사위를 다 사용한 경우
        answer = max(answer, sum(x_score))
        return
    else:
        if num < 4:    # 첫번째 말은 어느말이 되도 상관없다.
            for i in range(0, num + 1):  # 말 이동
                if x_point[i] == 32:
                    continue

                if x_point[i] in blue: # 파란색 위치에 있는 경우
                    next_point, add_score = move_cal_x(graph[x_point[i]][1], dice[num] - 1) # blue point 한칸 이동을 고려
                else:
                    next_point, add_score = move_cal_x(x_point[i], dice[num])

                if next_point == 32:    # 이동을 마친 경우
                    cur_point = x_point[i]
                    x_point[i] = 32
                    
                    DFS(num + 1)

                    x_point[i] = cur_point

                elif next_point in x_point:   # 겹치는 위치가 있는 경우
                    continue
                else:
                    cur_point = x_point[i]
                    x_point[i] = next_point
                    x_score[i] += add_score

                    # 다음 주사위 이동
                    DFS(num + 1)

                    # 원상복구
                    x_point[i] = cur_point
                    x_score[i] -= add_score
        else:
            for i in range(4):
                if x_point[i] == 32:
                    continue

                if x_point[i] in blue: # 파란색 위치에 있는 경우
                    next_point, add_score = move_cal_x(graph[x_point[i]][1], dice[num] - 1) # blue point 한칸 이동을 고려
                else:
                    next_point, add_score = move_cal_x(x_point[i], dice[num])

                if next_point == 32:    # 이동을 마친 경우
                    cur_point = x_point[i]
                    x_point[i] = 32

                    DFS(num + 1)

                    x_point[i] = cur_point

                elif next_point in x_point:   # 겹치는 위치가 있는 경우
                    continue
                else:
                    cur_point = x_point[i]
                    x_point[i] = next_point
                    x_score[i] += add_score

                    # 다음 주사위 이동
                    DFS(num + 1)

                    # 원상복구
                    x_point[i] = cur_point
                    x_score[i] -= add_score
                    

# graph의 index는 게임판의 위치, 반시계방향으로 돌아가면서 위치가 1씩 증가
# 파란색 부분은 21번째부터 왼, 아래, 우, 위 순으로 결정
score = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20,
         22, 24, 26, 28, 30, 32, 34, 36, 38, 40,
         13, 16, 19, 22, 24, 28, 27, 26, 25, 30,
         35, 0]

# 위치에 따른 다음 위치(시작:0, 도착:32)
graph = [[1], [2], [3], [4], [5],
         [6, 21], [7], [8], [9], [10],
         [11, 24], [12], [13], [14], [15], 
         [16, 26], [17], [18], [19], [20],
         [32], [22], [23], [29], [25], 
         [29], [27], [28], [29], [30],
         [31], [20]]

blue = [5, 10, 15]

dice = list(map(int, input().split()))
x_point = [0 for _ in range(4)]  # 말의 위치를 나타냄
x_score = [0 for _ in range(4)]  # 말의 점수를 나타냄

answer = 0
DFS(0)
print(answer)