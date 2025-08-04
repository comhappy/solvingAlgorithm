# N과 M(7)

def DFS(index):
    if len(result) == M:	# 일정 길이가 되면 출력
        print(" ".join(map(str, result)))

        return
    else:
        for i in range(0, N):	# 처음부터 시작, 중복을 허용
            result.append(num[i])
            DFS(i)
            result.pop()

        return

N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

result = list()
DFS(0)