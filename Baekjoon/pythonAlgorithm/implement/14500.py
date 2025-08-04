# 테트로미노

import sys, copy
input = sys.stdin.readline

# 1번 테트로미노 검사
def check_tetromino1(paper):
    max_num = 0

    for i in range(len(paper)): # 세로로 탐색   (세로개수 - 테트로미노의 세로길이 + 1)
        for j in range(len(paper[0]) - 3):
            num_sum = paper[i][j] + paper[i][j + 1] + paper[i][j + 2] + paper[i][j + 3]

            if num_sum > max_num:
                max_num = num_sum

    return max_num

# 2번 테트로미노 검사
def check_tetromino2(paper):
    max_num = 0

    for i in range(len(paper) - 1): # 세로로 탐색
        for j in range(len(paper[0]) - 1):
            num_sum = paper[i][j] + paper[i][j + 1] + paper[i + 1][j] + paper[i + 1][j + 1]

            if num_sum > max_num:
                max_num = num_sum

    return max_num

# 3번 테트로미노 검사
def check_tetromino3(paper):
    max_num = 0

    for i in range(len(paper) - 2): # 세로로 탐색
        for j in range(len(paper[0]) - 1):
            num_sum = paper[i][j] + paper[i + 1][j] + paper[i + 2][j] + paper[i + 2][j + 1]

            if num_sum > max_num:
                max_num = num_sum

    return max_num

# 4번 테트로미노 검사
def check_tetromino4(paper):
    max_num = 0

    for i in range(len(paper) - 2): # 세로로 탐색
        for j in range(len(paper[0]) - 1):
            num_sum = paper[i][j] + paper[i + 1][j] + paper[i + 1][j + 1] + paper[i + 2][j + 1]

            if num_sum > max_num:
                max_num = num_sum

    return max_num

# 5번 테트로미노 검사
def check_tetromino5(paper):
    max_num = 0

    for i in range(len(paper) - 1): # 세로로 탐색
        for j in range(len(paper[0]) - 2):
            num_sum = paper[i][j] + paper[i][j + 1] + paper[i][j + 2] + paper[i + 1][j + 1]

            if num_sum > max_num:
                max_num = num_sum

    return max_num


# 종이를 왼쪽으로 회전
def rotate_paper(paper):
    a = len(paper)  # N
    b = len(paper[0]) # M

    result_paper = [[0 for _ in range(a)] for _ in range(b)]

    for i in range(a):
        for j in range(b):
            x = j
            y = a - i - 1
        
            result_paper[x][y] = paper[i][j]

    return result_paper

# 종이를 반전
def over_paper(paper):
    a = len(paper)  # N
    b = len(paper[0]) # M

    result_paper = [[0 for _ in range(b)] for _ in range(a)]

    for i in range(a):
        for j in range(b):
            result_paper[i][b - 1 - j] = paper[i][j]

    return result_paper


# 5개의 테트로미노 종류가 있음. 회전, 대칭이 가능하므로 주어진 종이를 회전 대칭을 갈기자.
N, M = map(int, input().split())
paper = list(list(map(int, input().split())) for _ in range(N))

# 최댓값 구하기
re_paper = copy.deepcopy(paper)
answer = 0

for _ in range(4):
    for _ in range(2):
        result = list()

        result.append(check_tetromino1(re_paper))
        result.append(check_tetromino2(re_paper))
        result.append(check_tetromino3(re_paper))
        result.append(check_tetromino4(re_paper))
        result.append(check_tetromino5(re_paper))

        # 최댓값 구하기
        max_num = max(result)

        if max_num > answer:
            answer = max_num

        re_paper = over_paper(re_paper)
    
    re_paper = rotate_paper(re_paper)


print(answer)