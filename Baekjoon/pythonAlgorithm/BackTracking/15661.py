# 링크와 스타트

def cal_score(p):
    global start_score, link_score

    add_score = 0
    sub_score = 0

    for i in range(n):
        if start_team[i] == 1:
            add_score += (s[p][i] + s[i][p])
        else:
            sub_score += (s[p][i] + s[i][p])

    start_score += add_score
    link_score -= sub_score

    return abs(start_score - link_score)
    

def DFS(start):
    global answer

    for i in range(start, n):
        start_team[i] = 1
        answer = min(answer, cal_score(i))

        DFS(i + 1)
        start_team[i] = 0
        

n = int(input())
s = list(list(map(int, input().split())) for _ in range(n))

answer = 100 * (n ** 2)
start_team = [0 for _ in range(n)]
start_score = 0
link_score = sum(sum(i) for i in s)

DFS(0)

print(answer)