# 차이를 최대로

def DFS():
    if len(Alist) == N: # 가능한 경우, 계산 후 값 저장
        global answer

        result = 0

        # 값 계산
        for i in range(0, N - 1):
            result += abs(Alist[i] - Alist[i + 1])

        # 값 비교후 최대값 갱신
        if result > answer:
            answer = result

        return
    else:
        for i in range(N):
            if visited[i] == False: # 해당 숫자가 사용되지 않았으면 DFS 실행
                Alist.append(A[i])
                visited[i] = True

                DFS()

                Alist.pop()
                visited[i] = False

        return


N = int(input())
A = list(map(int, input().split()))
visited = [False for _ in range(N)]     # 중복된 숫자가 존재하기 때문에 확인할 배열이 필요함

Alist = list()
answer = 0

DFS()

print(answer)