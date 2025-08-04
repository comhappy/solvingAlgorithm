# 스타트와 링크

def DFS(p):     # p:팀에 들어오는 사람번호
    if len(team_start) == N // 2:    # 팀이 정해진 경우
        # teamp_list 구성
        for i in range(1, N+1):
            if i not in team_start:     # team_start에 없는 경우 추가
                team_link.append(i)
        
        # 능력치 계산
        score = 0

        for i in team_start:
            for j in team_start:
                score += graph[i - 1][j - 1]
                    

        for i in team_link:
            for j in team_link:
                score -= graph[i - 1][j - 1]

        if score < 0:   # 점수가 음수인 경우 양수로 저장
            score *= -1

        result.append(score)
        team_link.clear()

    else:   # 팀이 정해지지 않은 경우
        for i in range(p, N + 1):
            if i not in team_start: # 번호가 같은 경우를 제외
                team_start.append(i)
                DFS(i)
                team_start.pop() 

N = int(input())
graph = list()

for _ in range(N):
    graph.append(list(map(int, input().split())))

team_start = list()
team_link = list()
result = list()

DFS(1)

print(min(result))