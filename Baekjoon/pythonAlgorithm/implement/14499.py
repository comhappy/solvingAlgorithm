# 주사위 굴리기

def move_dice(dir): # 주사위 이동
    if dir == 1:    # 동쪽이동
        temp = dice[0]
        dice[0] = dice[2]
        dice[2] = dice[5]
        dice[5] = dice[3]
        dice[3] = temp
        
    elif dir == 2:    # 서쪽이동
        temp = dice[0]
        dice[0] = dice[3]
        dice[3] = dice[5]
        dice[5] = dice[2]
        dice[2] = temp   

    elif dir == 3:    # 북쪽이동
        temp = dice[0]
        dice[0] = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[4]
        dice[4] = temp

    elif dir == 4:    # 남쪽이동
        temp = dice[0]
        dice[0] = dice[4]
        dice[4] = dice[5]
        dice[5] = dice[1]
        dice[1] = temp

def number_dice():  # 주사위 숫자 작성
    if graph[x][y] == 0:
        graph[x][y] = dice[0]
    else:
        dice[0] = graph[x][y]
        graph[x][y] = 0

# 입력
n, m, x, y, k = map(int, input().split())
graph = list(list(map(int, input().split())) for _ in range(n))
a = list(map(int, input().split()))

dice = [0 for _ in range(6)]    # 주사위 결정
#   1
# 3 0 2     숫자의 index를 나타냄
#   4
#   5

for i in a:
    if i == 1:  # 동쪽으로 이동
        if 0 <= y + 1 < m:
            y = y + 1
            move_dice(i)
            number_dice()
            print(dice[5])
    elif i == 2:  # 서쪽으로 이동
        if 0 <= y - 1 < m:
            y = y - 1
            move_dice(i)
            number_dice()
            print(dice[5])
    elif i == 3:  # 북쪽으로 이동
        if 0 <= x - 1 < n:
            x = x - 1
            move_dice(i)
            number_dice()
            print(dice[5])
    elif i == 4:  # 남쪽으로 이동
        if 0 <= x + 1 < n:
            x = x + 1
            move_dice(i)
            number_dice()
            print(dice[5])