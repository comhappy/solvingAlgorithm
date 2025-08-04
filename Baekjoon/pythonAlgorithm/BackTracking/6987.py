# 월드컵

import copy

def DFS(n, match):  # 경기정보를 구하는 DFS
    if len(match) == 2:
        matchinfo.append(copy.deepcopy(match))
    else:
        for i in range(n, 6):
            if visited[i] == 0 and i != n:
                visited[i] = 1
                match.append(i)
                DFS(i, match)
                visited[i] = 0
                match.pop()

def checkmatch(team1, team2):
    # 경기가 성립되지 않는 경우
    for i in range(3):
        if info[team1][i] < 0 or info[team2][i] < 0:
            return False
    
    return True


def match(depth):   # n번째 경기, result 결과
    global answer

    if answer == 1: # 가능한 결과가 나온 경우, 더 이상 탐색할 필요가 없음
        return
    elif depth == 15:   # 모든 경기를 고려한 경우
        temp = 0

        for i in info:
            temp += sum(i)

        if temp == 0:
            answer = 1

        return
    else:
        team1 = matchinfo[depth][0]
        team2 = matchinfo[depth][1]

        # i번째 경기에서 첫번째 팀이 이기는 경우
        info[team1][0] -= 1
        info[team2][2] -= 1
        if checkmatch(team1, team2):
            match(depth + 1)
        info[team1][0] += 1
        info[team2][2] += 1

        # i번째 경기에서 첫번째 팀이 지는 경우
        info[team1][2] -= 1
        info[team2][0] -= 1
        if checkmatch(team1, team2):
            match(depth + 1)
        info[team1][2] += 1
        info[team2][0] += 1

        # i번째 경기에서 무승부인 경우
        info[team1][1] -= 1
        info[team2][1] -= 1
        if checkmatch(team1, team2):
            match(depth + 1)
        info[team1][1] += 1
        info[team2][1] += 1


matchinfo = list()
visited = [0 for _ in range(6)]
DFS(-1, [])

for _ in range(4):
    info = list(map(int, input().split()))
    info = [info[i:i+3] for i in range(0, 18, 3)]

    answer = 0
    match(0)
    print(answer, end=' ')