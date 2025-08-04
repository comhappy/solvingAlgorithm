# 로마 숫자 만들기
# 조합의 경우를 세는것임(순서가 상관없다고 함함)

def DFS(before, depth, num):
    if depth == n:
        visited[num] = 1
        return
    else:
        for i in range(before, 4):
            DFS(i, depth + 1, num + IVXL[i])

n = int(input())
visited =[0 for _ in range(n * 50 + 1)] # index는 만들 수 있는 수를 뜻함
IVXL = [1, 5, 10, 50]

DFS(0, 0, 0)
print(sum(visited))